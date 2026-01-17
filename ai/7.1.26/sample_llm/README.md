# Sample LLM - A Minimal Language Model Implementation

A simple yet functional Large Language Model (LLM) implementation from scratch using PyTorch. This project demonstrates the core concepts of building a transformer-based language model.

## 🎯 Features

- **Transformer Architecture**: Multi-head self-attention, feed-forward networks, layer normalization
- **Custom Tokenizer**: Simple word-level tokenizer with special tokens
- **Training Pipeline**: Complete training loop with validation and checkpointing
- **Text Generation**: Autoregressive generation with temperature and top-k sampling
- **Interactive Mode**: Chat-like interface for experimenting with the model

## 📁 Project Structure

```
sample_llm/
├── model.py          # Transformer model architecture
├── tokenizer.py      # Simple tokenizer implementation
├── dataset.py        # Dataset and dataloader utilities
├── train.py          # Training script
├── generate.py       # Text generation script
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

```bash
python train.py
```

This will:
- Train a tokenizer on sample data
- Initialize a small transformer model (~10M parameters)
- Train for 50 epochs with validation
- Save checkpoints to `checkpoints/` directory

**Training Configuration:**
- Model size: 256 hidden dimensions, 8 attention heads, 6 layers
- Vocabulary: 2000 tokens
- Context length: 512 tokens
- Batch size: 8
- Learning rate: 3e-4 with cosine annealing

### 3. Generate Text

**Single prompt generation:**
```bash
python generate.py --prompt "Machine learning is"
```

**Interactive mode:**
```bash
python generate.py --interactive
```

**Sample generations (default):**
```bash
python generate.py
```

**Custom parameters:**
```bash
python generate.py --prompt "Deep learning" --max_tokens 150 --temperature 0.9 --top_k 40
```

## 🧠 Model Architecture

### SimpleLLM Components

1. **Token Embedding**: Maps token IDs to dense vectors
2. **Position Embedding**: Adds positional information to tokens
3. **Transformer Blocks** (6 layers):
   - Multi-head self-attention (8 heads)
   - Feed-forward network (4x expansion)
   - Layer normalization (pre-norm)
   - Residual connections
4. **Output Projection**: Maps hidden states to vocabulary logits

### Key Features

- **Causal Masking**: Prevents attention to future tokens
- **Gradient Clipping**: Stabilizes training
- **Dropout**: Regularization (0.1)
- **Weight Initialization**: Proper initialization for stable training

## 📊 Model Statistics

```
Parameters: ~10M
Vocabulary Size: 2000 tokens
Context Length: 512 tokens
Hidden Dimension: 256
Attention Heads: 8
Layers: 6
Feed-Forward Dimension: 1024
```

## 🎮 Generation Parameters

- **temperature**: Controls randomness (0.1-2.0)
  - Lower = more deterministic
  - Higher = more creative/random
  - Default: 0.8

- **top_k**: Limits sampling to top K tokens
  - Lower = more focused
  - Higher = more diverse
  - Default: 50

- **max_tokens**: Maximum tokens to generate
  - Default: 100

## 📝 Example Usage

### Training

```python
from model import SimpleLLM
from tokenizer import SimpleTokenizer
from dataset import get_sample_data, create_dataloader

# Load data
texts = get_sample_data()

# Train tokenizer
tokenizer = SimpleTokenizer(vocab_size=2000)
tokenizer.train(texts)

# Create model
model = SimpleLLM(
    vocab_size=len(tokenizer.word_to_id),
    d_model=256,
    num_heads=8,
    num_layers=6
)

# Train model
# (see train.py for complete training loop)
```

### Inference

```python
from model import SimpleLLM
from tokenizer import SimpleTokenizer
import torch

# Load model and tokenizer
tokenizer = SimpleTokenizer()
tokenizer.load('checkpoints/tokenizer.pkl')

checkpoint = torch.load('checkpoints/best_model.pt')
model = SimpleLLM(**checkpoint['model_config'])
model.load_state_dict(checkpoint['model_state_dict'])

# Generate text
prompt = "Machine learning is"
input_ids = torch.tensor([tokenizer.encode(prompt)])
output_ids = model.generate(input_ids, max_new_tokens=50)
text = tokenizer.decode(output_ids[0].tolist())
print(text)
```

## 🔧 Customization

### Modify Model Size

Edit `train.py`:

```python
model = SimpleLLM(
    vocab_size=len(tokenizer.word_to_id),
    d_model=512,        # Increase hidden dimension
    num_heads=16,       # More attention heads
    num_layers=12,      # Deeper model
    d_ff=2048,          # Larger feed-forward
    max_seq_len=1024,   # Longer context
)
```

### Use Custom Data

Edit `dataset.py`:

```python
def get_sample_data():
    # Load your own text data
    with open('your_data.txt', 'r') as f:
        texts = f.readlines()
    return texts
```

### Adjust Training

Edit `train.py`:

```python
num_epochs = 100           # More epochs
learning_rate = 1e-4       # Different learning rate
batch_size = 16            # Larger batches
max_length = 128           # Longer sequences
```

## 📈 Training Tips

1. **Monitor Loss**: Training loss should decrease steadily
2. **Check Perplexity**: Lower is better (good models: <20)
3. **Validation**: Watch for overfitting (val loss increasing)
4. **Generation Quality**: Test periodically during training
5. **Learning Rate**: Reduce if loss is unstable
6. **Batch Size**: Increase for faster training (if GPU memory allows)

## 🐛 Troubleshooting

**Out of Memory:**
- Reduce batch size
- Reduce model size (d_model, num_layers)
- Reduce max_seq_len
- Enable gradient checkpointing

**Poor Generation Quality:**
- Train longer (more epochs)
- Use more/better training data
- Increase model size
- Adjust temperature/top_k

**Training Instability:**
- Reduce learning rate
- Enable gradient clipping
- Check for NaN values
- Verify data quality

## 🎓 Learning Resources

This implementation demonstrates:
- Transformer architecture basics
- Self-attention mechanism
- Autoregressive language modeling
- Training and inference pipelines
- Text generation strategies

**Next Steps:**
- Add more training data
- Implement beam search
- Add evaluation metrics (BLEU, perplexity)
- Try different architectures (GPT-2, LLaMA-style)
- Implement fine-tuning capabilities

## 📄 License

This is a educational project for learning purposes.

## 🙏 Acknowledgments

Based on concepts from:
- "Attention Is All You Need" (Vaswani et al.)
- GPT architecture (OpenAI)
- Various open-source implementations

---

**Happy Learning! 🚀**
