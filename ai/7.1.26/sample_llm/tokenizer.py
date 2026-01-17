import re
from collections import Counter
import pickle


class SimpleTokenizer:
    def __init__(self, vocab_size=5000):
        self.vocab_size = vocab_size
        self.word_to_id = {}
        self.id_to_word = {}
        self.special_tokens = {
            '<PAD>': 0,
            '<UNK>': 1,
            '<BOS>': 2,
            '<EOS>': 3,
        }
        self.word_to_id.update(self.special_tokens)
        self.id_to_word = {v: k for k, v in self.word_to_id.items()}
        
    def train(self, texts):
        all_words = []
        for text in texts:
            words = self._tokenize_text(text)
            all_words.extend(words)
        
        word_counts = Counter(all_words)
        most_common = word_counts.most_common(self.vocab_size - len(self.special_tokens))
        
        for idx, (word, _) in enumerate(most_common, start=len(self.special_tokens)):
            self.word_to_id[word] = idx
            self.id_to_word[idx] = word
        
        print(f"Vocabulary size: {len(self.word_to_id)}")
        
    def _tokenize_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s.,!?;:\'\"-]', '', text)
        words = re.findall(r'\b\w+\b|[.,!?;:\'\"-]', text)
        return words
    
    def encode(self, text, add_special_tokens=True):
        words = self._tokenize_text(text)
        token_ids = []
        
        if add_special_tokens:
            token_ids.append(self.special_tokens['<BOS>'])
        
        for word in words:
            token_id = self.word_to_id.get(word, self.special_tokens['<UNK>'])
            token_ids.append(token_id)
        
        if add_special_tokens:
            token_ids.append(self.special_tokens['<EOS>'])
        
        return token_ids
    
    def decode(self, token_ids, skip_special_tokens=True):
        words = []
        for token_id in token_ids:
            word = self.id_to_word.get(token_id, '<UNK>')
            if skip_special_tokens and word in self.special_tokens:
                continue
            words.append(word)
        
        text = ' '.join(words)
        text = re.sub(r'\s+([.,!?;:\'\"-])', r'\1', text)
        return text
    
    def save(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump({
                'vocab_size': self.vocab_size,
                'word_to_id': self.word_to_id,
                'id_to_word': self.id_to_word,
                'special_tokens': self.special_tokens
            }, f)
        print(f"Tokenizer saved to {filepath}")
    
    def load(self, filepath):
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        self.vocab_size = data['vocab_size']
        self.word_to_id = data['word_to_id']
        self.id_to_word = data['id_to_word']
        self.special_tokens = data['special_tokens']
        print(f"Tokenizer loaded from {filepath}")


if __name__ == "__main__":
    sample_texts = [
        "Hello, how are you today?",
        "I am learning to build a language model.",
        "This is a simple tokenizer for demonstration.",
        "Machine learning is fascinating!",
    ]
    
    tokenizer = SimpleTokenizer(vocab_size=100)
    tokenizer.train(sample_texts)
    
    text = "Hello, I am learning machine learning!"
    encoded = tokenizer.encode(text)
    decoded = tokenizer.decode(encoded)
    
    print(f"\nOriginal: {text}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
