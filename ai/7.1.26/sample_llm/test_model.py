import torch
from model import SimpleLLM
from tokenizer import SimpleTokenizer

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}\n")

print("Loading tokenizer...")
tokenizer = SimpleTokenizer()
tokenizer.load('checkpoints/tokenizer.pkl')

print("Loading checkpoint...")
checkpoint = torch.load('checkpoints/best_model.pt', map_location=device)

print(f"\nCheckpoint Info:")
print(f"  Epoch: {checkpoint['epoch']}")
print(f"  Loss: {checkpoint['loss']:.4f}")
print(f"  Vocab Size: {checkpoint['model_config']['vocab_size']}")

config = checkpoint['model_config']
model = SimpleLLM(
    vocab_size=config['vocab_size'],
    d_model=config['d_model'],
    num_heads=config['num_heads'],
    num_layers=config['num_layers'],
    d_ff=config['d_ff'],
    max_seq_len=config['max_seq_len'],
    dropout=0.0
).to(device)

model.load_state_dict(checkpoint['model_state_dict'])
model.eval()

print("\n" + "="*60)
print("Testing Generation with Different Settings")
print("="*60)

prompts = [
    "Machine learning",
    "The transformer",
    "Deep learning",
]

for prompt in prompts:
    print(f"\n--- Prompt: '{prompt}' ---")
    
    input_ids = tokenizer.encode(prompt, add_special_tokens=True)
    input_ids = torch.tensor([input_ids], dtype=torch.long).to(device)
    
    with torch.no_grad():
        generated = model.generate(
            input_ids,
            max_new_tokens=30,
            temperature=0.7,
            top_k=20
        )
    
    text = tokenizer.decode(generated[0].tolist(), skip_special_tokens=True)
    print(text)

print("\n" + "="*60)
print("Testing with Greedy Decoding (temperature=0.1)")
print("="*60)

prompt = "Machine learning is"
print(f"\nPrompt: '{prompt}'")

input_ids = tokenizer.encode(prompt, add_special_tokens=True)
input_ids = torch.tensor([input_ids], dtype=torch.long).to(device)

with torch.no_grad():
    generated = model.generate(
        input_ids,
        max_new_tokens=30,
        temperature=0.1,
        top_k=10
    )

text = tokenizer.decode(generated[0].tolist(), skip_special_tokens=True)
print(text)
