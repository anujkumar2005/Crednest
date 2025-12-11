
import torch
import transformers
import tokenizers
from transformers import AutoTokenizer

print(f"PyTorch version: {torch.__version__}")
print(f"Transformers version: {transformers.__version__}")
print(f"Tokenizers version: {tokenizers.__version__}")

model_name = "mistralai/Mistral-7B-v0.1"
print(f"Attempting to load tokenizer for {model_name}...")

try:
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    print("Successfully loaded tokenizer.")
except Exception as e:
    print(f"Error loading tokenizer: {e}")
