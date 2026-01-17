import torch
from torch.utils.data import Dataset, DataLoader


class TextDataset(Dataset):
    def __init__(self, texts, tokenizer, max_length=128):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.examples = []
        self.pad_id = tokenizer.special_tokens['<PAD>']
        
        for text in texts:
            token_ids = tokenizer.encode(text, add_special_tokens=True)
            
            if len(token_ids) >= max_length:
                for i in range(0, len(token_ids) - max_length + 1, max_length // 2):
                    chunk = token_ids[i:i + max_length]
                    self.examples.append(chunk)
            elif len(token_ids) > 5:
                padded = token_ids + [self.pad_id] * (max_length - len(token_ids))
                self.examples.append(padded)
        
        print(f"Created dataset with {len(self.examples)} examples")
    
    def __len__(self):
        return len(self.examples)
    
    def __getitem__(self, idx):
        token_ids = self.examples[idx]
        input_ids = torch.tensor(token_ids[:-1], dtype=torch.long)
        target_ids = torch.tensor(token_ids[1:], dtype=torch.long)
        target_ids[target_ids == self.pad_id] = -100
        return input_ids, target_ids


def get_sample_data():
    texts = [
        "Machine learning is a branch of artificial intelligence that enables computers to learn from data without being explicitly programmed. It uses algorithms to identify patterns and make predictions based on historical information.",
        "Deep learning is a subset of machine learning that uses neural networks with multiple layers to process complex data. These networks can automatically learn hierarchical representations of features from raw input.",
        "Natural language processing allows computers to understand, interpret, and generate human language. It combines computational linguistics with machine learning to enable applications like chatbots, translation, and sentiment analysis.",
        "The transformer architecture revolutionized natural language processing by introducing the attention mechanism. This allows models to weigh the importance of different words in a sentence when making predictions.",
        "Attention mechanisms help neural networks focus on relevant parts of the input when processing sequences. Multi-head attention allows the model to attend to information from different representation subspaces simultaneously.",
        "Large language models are trained on massive amounts of text data to learn patterns in human language. They can generate coherent text, answer questions, and perform various language tasks with impressive accuracy.",
        "Training neural networks requires careful tuning of hyperparameters like learning rate, batch size, and number of epochs. The learning rate controls how much the model parameters are updated during each training step.",
        "Gradient descent is an optimization algorithm that minimizes the loss function by iteratively adjusting model parameters in the direction of steepest descent. Variants like Adam and SGD offer different trade-offs between speed and stability.",
        "Backpropagation is the algorithm used to compute gradients in neural networks. It applies the chain rule of calculus to efficiently calculate how each parameter affects the final loss.",
        "Overfitting occurs when a model learns the training data too well, including its noise and peculiarities, resulting in poor performance on new unseen data. Regularization techniques help prevent this problem.",
        "Regularization methods like dropout, weight decay, and early stopping help prevent overfitting by adding constraints to the model. Dropout randomly deactivates neurons during training to improve generalization.",
        "Layer normalization stabilizes neural network training by normalizing the activations within each layer. This helps gradients flow more smoothly through deep networks and enables faster convergence.",
        "Positional encoding adds information about token positions to the input embeddings in transformer models. This is necessary because the attention mechanism itself has no inherent notion of sequence order.",
        "The feed-forward network in each transformer layer processes each position independently using two linear transformations with a non-linear activation function in between. This adds expressiveness to the model.",
        "Residual connections allow information to skip layers in deep neural networks, helping gradients flow through the network during backpropagation. This enables training of much deeper architectures.",
        "Tokenization is the process of breaking text into smaller units like words, subwords, or characters. Modern language models often use subword tokenization methods like Byte-Pair Encoding or WordPiece.",
        "Word embeddings represent words as dense vectors in a continuous space where semantically similar words are close together. These representations capture semantic relationships and enable mathematical operations on words.",
        "The softmax function converts a vector of real numbers into a probability distribution. It is commonly used in the output layer of classification models to produce class probabilities.",
        "Cross-entropy loss measures the difference between predicted probability distributions and actual distributions. It is the standard loss function for classification tasks in machine learning.",
        "Batch size determines how many training examples are processed together before updating model parameters. Larger batches provide more stable gradients but require more memory.",
        "The vocabulary size determines how many unique tokens a language model can recognize and generate. Larger vocabularies can represent more words but require more parameters and memory.",
        "Temperature is a parameter that controls the randomness of text generation. Lower temperatures make the model more confident and deterministic, while higher temperatures increase diversity and creativity.",
        "Top-k sampling restricts text generation to only the k most likely next tokens at each step. This helps prevent the model from selecting very unlikely words while maintaining some randomness.",
        "Beam search is a generation strategy that explores multiple possible sequences simultaneously, keeping track of the most promising candidates. It often produces better results than greedy decoding.",
        "Perplexity is a metric that measures how well a language model predicts a sample of text. Lower perplexity indicates better performance, as the model is less surprised by the actual text.",
        "The context window defines the maximum number of tokens a model can consider at once. Longer context windows allow the model to capture dependencies over greater distances in the text.",
        "Autoregressive models generate sequences one token at a time, using previously generated tokens as context for predicting the next token. This approach is used in models like GPT.",
        "Causal masking ensures that when predicting a token, the model can only attend to previous tokens, not future ones. This is essential for autoregressive language modeling.",
        "The decoder architecture is specifically designed for sequence generation tasks. It uses causal masking to ensure that predictions only depend on previous tokens in the sequence.",
        "Encoder-decoder architectures are used for sequence-to-sequence tasks like translation. The encoder processes the input sequence, and the decoder generates the output sequence based on the encoded representation.",
        "Self-attention computes relationships between all pairs of tokens in a sequence by calculating attention scores. This allows the model to capture long-range dependencies effectively.",
        "Scaled dot-product attention divides the attention scores by the square root of the dimension to prevent the softmax function from having extremely small gradients in high-dimensional spaces.",
        "Query, key, and value matrices are learned linear projections of the input in the attention mechanism. The query and key determine attention weights, while the value contains the information to be aggregated.",
        "The output projection layer maps the hidden states from the final transformer layer back to the vocabulary space, producing logits for each possible token.",
        "Inference is the process of using a trained model to make predictions on new data. During inference, the model operates in evaluation mode with dropout and other training-specific techniques disabled.",
        "Checkpointing saves model weights and optimizer state periodically during training. This allows resuming training from a saved point if interrupted and enables selecting the best model based on validation performance.",
        "Early stopping is a regularization technique that halts training when validation performance stops improving. This prevents overfitting and saves computational resources.",
        "Data augmentation creates variations of training examples to artificially increase dataset size and improve model robustness. Techniques include paraphrasing, back-translation, and random perturbations.",
        "Transfer learning leverages knowledge learned from one task to improve performance on a related task. Pre-trained language models can be fine-tuned on specific tasks with much less data.",
        "Zero-shot learning enables models to perform tasks they were not explicitly trained on by leveraging their general language understanding. This is a key capability of large language models.",
        "Few-shot learning allows models to adapt to new tasks using only a small number of examples. In-context learning in large language models demonstrates impressive few-shot capabilities.",
        "Prompt engineering is the practice of carefully designing input text to elicit desired behaviors from language models. Well-crafted prompts can significantly improve model performance on specific tasks.",
        "In-context learning allows language models to learn from examples provided directly in the input prompt without updating model parameters. This enables flexible task adaptation at inference time.",
        "Instruction tuning trains language models to follow natural language instructions by fine-tuning on datasets of instruction-response pairs. This improves their ability to understand and execute user requests.",
        "Fine-tuning adapts pre-trained models to specific downstream tasks by continuing training on task-specific data. This typically requires much less data and computation than training from scratch.",
        "Pre-training on large text corpora helps language models learn general patterns in language, including grammar, facts, and reasoning abilities. This knowledge can then be transferred to various downstream tasks.",
        "The learning rate schedule determines how the learning rate changes during training. Common schedules include constant, linear decay, and cosine annealing, each with different convergence properties.",
        "Gradient clipping prevents exploding gradients by limiting the magnitude of gradient updates. This is especially important when training recurrent networks or very deep architectures.",
        "Weight initialization is crucial for successful neural network training. Proper initialization helps prevent vanishing or exploding gradients and enables faster convergence to good solutions.",
        "Activation functions introduce non-linearity into neural networks, enabling them to learn complex patterns. Common choices include ReLU, GELU, and Swish, each with different properties.",
    ]
    return texts


def create_dataloader(texts, tokenizer, max_length=128, batch_size=8, shuffle=True):
    dataset = TextDataset(texts, tokenizer, max_length)
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=0,
        pin_memory=True
    )
    return dataloader


if __name__ == "__main__":
    from tokenizer import SimpleTokenizer
    
    texts = get_sample_data()
    
    tokenizer = SimpleTokenizer(vocab_size=1000)
    tokenizer.train(texts)
    
    dataloader = create_dataloader(texts, tokenizer, max_length=64, batch_size=4)
    
    for batch_idx, (input_ids, target_ids) in enumerate(dataloader):
        print(f"\nBatch {batch_idx + 1}:")
        print(f"Input shape: {input_ids.shape}")
        print(f"Target shape: {target_ids.shape}")
        print(f"Sample input: {input_ids[0][:10].tolist()}")
        
        if batch_idx >= 2:
            break
