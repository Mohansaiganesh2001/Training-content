import torch
import torch.nn as nn
from torch.optim import AdamW
from torch.optim.lr_scheduler import CosineAnnealingLR
import os
import time
from tqdm import tqdm

from model import SimpleLLM, count_parameters
from tokenizer import SimpleTokenizer
from dataset import get_sample_data, create_dataloader


def train_epoch(model, dataloader, optimizer, scheduler, device, epoch):
    model.train()
    total_loss = 0
    num_batches = len(dataloader)
    
    progress_bar = tqdm(dataloader, desc=f"Epoch {epoch}")
    
    for batch_idx, (input_ids, target_ids) in enumerate(progress_bar):
        input_ids = input_ids.to(device)
        target_ids = target_ids.to(device)
        
        optimizer.zero_grad()
        
        logits, loss = model(input_ids, targets=target_ids)
        
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        scheduler.step()
        
        total_loss += loss.item()
        
        progress_bar.set_postfix({
            'loss': f'{loss.item():.4f}',
            'avg_loss': f'{total_loss / (batch_idx + 1):.4f}',
            'lr': f'{scheduler.get_last_lr()[0]:.6f}'
        })
    
    avg_loss = total_loss / num_batches
    return avg_loss


def evaluate(model, dataloader, device):
    model.eval()
    total_loss = 0
    num_batches = len(dataloader)
    
    with torch.no_grad():
        for input_ids, target_ids in dataloader:
            input_ids = input_ids.to(device)
            target_ids = target_ids.to(device)
            
            logits, loss = model(input_ids, targets=target_ids)
            total_loss += loss.item()
    
    avg_loss = total_loss / num_batches
    perplexity = torch.exp(torch.tensor(avg_loss)).item()
    return avg_loss, perplexity


def save_checkpoint(model, tokenizer, optimizer, epoch, loss, filepath):
    checkpoint = {
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': loss,
        'model_config': {
            'vocab_size': model.token_embedding.num_embeddings,
            'd_model': model.d_model,
            'num_heads': model.transformer_blocks[0].attention.num_heads,
            'num_layers': len(model.transformer_blocks),
            'd_ff': model.transformer_blocks[0].feed_forward.linear1.out_features,
            'max_seq_len': model.max_seq_len,
        }
    }
    torch.save(checkpoint, filepath)
    print(f"Checkpoint saved to {filepath}")


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    print("\n=== Loading Data ===")
    texts = get_sample_data()
    print(f"Loaded {len(texts)} text samples")
    
    print("\n=== Training Tokenizer ===")
    tokenizer = SimpleTokenizer(vocab_size=3000)
    tokenizer.train(texts)
    
    os.makedirs('checkpoints', exist_ok=True)
    tokenizer.save('checkpoints/tokenizer.pkl')
    
    print("\n=== Creating Dataloaders ===")
    train_size = int(0.9 * len(texts))
    train_texts = texts[:train_size]
    val_texts = texts[train_size:]
    
    train_dataloader = create_dataloader(
        train_texts, tokenizer, max_length=64, batch_size=4, shuffle=True
    )
    val_dataloader = create_dataloader(
        val_texts, tokenizer, max_length=64, batch_size=4, shuffle=False
    )
    
    print("\n=== Initializing Model ===")
    model = SimpleLLM(
        vocab_size=len(tokenizer.word_to_id),
        d_model=256,
        num_heads=8,
        num_layers=6,
        d_ff=1024,
        max_seq_len=512,
        dropout=0.1
    ).to(device)
    
    print(f"Model Parameters: {count_parameters(model):,}")
    
    print("\n=== Training Configuration ===")
    num_epochs = 100
    learning_rate = 5e-4
    warmup_steps = 100
    
    optimizer = AdamW(model.parameters(), lr=learning_rate, weight_decay=0.01)
    total_steps = len(train_dataloader) * num_epochs
    scheduler = CosineAnnealingLR(optimizer, T_max=total_steps, eta_min=1e-6)
    
    print(f"Epochs: {num_epochs}")
    print(f"Learning Rate: {learning_rate}")
    print(f"Total Training Steps: {total_steps}")
    
    print("\n=== Starting Training ===")
    best_val_loss = float('inf')
    
    for epoch in range(1, num_epochs + 1):
        print(f"\n{'='*50}")
        print(f"Epoch {epoch}/{num_epochs}")
        print(f"{'='*50}")
        
        start_time = time.time()
        train_loss = train_epoch(model, train_dataloader, optimizer, scheduler, device, epoch)
        epoch_time = time.time() - start_time
        
        val_loss, val_perplexity = evaluate(model, val_dataloader, device)
        
        print(f"\nEpoch {epoch} Summary:")
        print(f"  Train Loss: {train_loss:.4f}")
        print(f"  Val Loss: {val_loss:.4f}")
        print(f"  Val Perplexity: {val_perplexity:.2f}")
        print(f"  Time: {epoch_time:.2f}s")
        
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            save_checkpoint(
                model, tokenizer, optimizer, epoch, val_loss,
                'checkpoints/best_model.pt'
            )
            print(f"  ✓ New best model saved!")
        
        if epoch % 10 == 0:
            save_checkpoint(
                model, tokenizer, optimizer, epoch, val_loss,
                f'checkpoints/model_epoch_{epoch}.pt'
            )
    
    print("\n=== Training Complete ===")
    print(f"Best Validation Loss: {best_val_loss:.4f}")
    print(f"Best Validation Perplexity: {torch.exp(torch.tensor(best_val_loss)):.2f}")


if __name__ == "__main__":
    main()
