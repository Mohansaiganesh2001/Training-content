import torch
import argparse

from model import SimpleLLM
from tokenizer import SimpleTokenizer


def load_model(checkpoint_path, device):
    checkpoint = torch.load(checkpoint_path, map_location=device)
    
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
    
    print(f"Model loaded from {checkpoint_path}")
    print(f"Trained for {checkpoint['epoch']} epochs")
    print(f"Final loss: {checkpoint['loss']:.4f}")
    
    return model


def generate_text(model, tokenizer, prompt, max_new_tokens=100, temperature=0.8, top_k=50, device='cpu'):
    model.eval()
    
    input_ids = tokenizer.encode(prompt, add_special_tokens=True)
    input_ids = torch.tensor([input_ids], dtype=torch.long).to(device)
    
    print(f"\nPrompt: {prompt}")
    print(f"Generating {max_new_tokens} tokens...\n")
    print("="*60)
    
    with torch.no_grad():
        generated_ids = model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_k=top_k
        )
    
    generated_text = tokenizer.decode(generated_ids[0].tolist(), skip_special_tokens=True)
    
    print(generated_text)
    print("="*60)
    
    return generated_text


def interactive_mode(model, tokenizer, device, temperature=0.8, top_k=50, max_tokens=100):
    print("\n" + "="*60)
    print("Interactive Text Generation Mode")
    print("="*60)
    print("Commands:")
    print("  - Type your prompt and press Enter to generate")
    print("  - Type 'quit' or 'exit' to stop")
    print("  - Type 'temp X' to change temperature (e.g., 'temp 0.7')")
    print("  - Type 'topk X' to change top-k (e.g., 'topk 40')")
    print("  - Type 'tokens X' to change max tokens (e.g., 'tokens 150')")
    print("="*60 + "\n")
    
    while True:
        try:
            user_input = input("\nPrompt: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if user_input.startswith('temp '):
                try:
                    temperature = float(user_input.split()[1])
                    print(f"Temperature set to {temperature}")
                except:
                    print("Invalid temperature value")
                continue
            
            if user_input.startswith('topk '):
                try:
                    top_k = int(user_input.split()[1])
                    print(f"Top-k set to {top_k}")
                except:
                    print("Invalid top-k value")
                continue
            
            if user_input.startswith('tokens '):
                try:
                    max_tokens = int(user_input.split()[1])
                    print(f"Max tokens set to {max_tokens}")
                except:
                    print("Invalid max tokens value")
                continue
            
            if not user_input:
                print("Please enter a prompt")
                continue
            
            generate_text(
                model, tokenizer, user_input,
                max_new_tokens=max_tokens,
                temperature=temperature,
                top_k=top_k,
                device=device
            )
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description='Generate text using trained LLM')
    parser.add_argument('--checkpoint', type=str, default='checkpoints/best_model.pt',
                        help='Path to model checkpoint')
    parser.add_argument('--tokenizer', type=str, default='checkpoints/tokenizer.pkl',
                        help='Path to tokenizer file')
    parser.add_argument('--prompt', type=str, default=None,
                        help='Text prompt for generation')
    parser.add_argument('--max_tokens', type=int, default=100,
                        help='Maximum number of tokens to generate')
    parser.add_argument('--temperature', type=float, default=0.8,
                        help='Sampling temperature (higher = more random)')
    parser.add_argument('--top_k', type=int, default=50,
                        help='Top-k sampling parameter')
    parser.add_argument('--interactive', action='store_true',
                        help='Run in interactive mode')
    
    args = parser.parse_args()
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    print("\nLoading tokenizer...")
    tokenizer = SimpleTokenizer()
    tokenizer.load(args.tokenizer)
    
    print("\nLoading model...")
    model = load_model(args.checkpoint, device)
    
    if args.interactive:
        interactive_mode(model, tokenizer, device, args.temperature, args.top_k, args.max_tokens)
    else:
        if args.prompt is None:
            prompts = [
                "Machine learning is",
                "The transformer architecture",
                "Deep learning uses",
                "Natural language processing",
            ]
            
            print("\n" + "="*60)
            print("Running sample generations")
            print("="*60)
            
            for prompt in prompts:
                generate_text(
                    model, tokenizer, prompt,
                    max_new_tokens=args.max_tokens,
                    temperature=args.temperature,
                    top_k=args.top_k,
                    device=device
                )
                print()
        else:
            generate_text(
                model, tokenizer, args.prompt,
                max_new_tokens=args.max_tokens,
                temperature=args.temperature,
                top_k=args.top_k,
                device=device
            )


if __name__ == "__main__":
    main()
