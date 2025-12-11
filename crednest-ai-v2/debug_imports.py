
print("Importing torch...")
import torch
print("Success.")

print("Importing transformers...")
import transformers
print("Success.")

print("Importing AutoModelForCausalLM...")
try:
    from transformers import AutoModelForCausalLM
    print("Success.")
except ImportError as e:
    print(f"Failed: {e}")

print("Importing AutoTokenizer...")
try:
    from transformers import AutoTokenizer
    print("Success.")
except ImportError as e:
    print(f"Failed: {e}")

print("Importing BitsAndBytesConfig...")
try:
    from transformers import BitsAndBytesConfig
    print("Success.")
except ImportError as e:
    print(f"Failed: {e}")

print("Importing TrainingArguments...")
try:
    from transformers import TrainingArguments
    print("Success.")
except ImportError as e:
    print(f"Failed: {e}")

print("Importing peft...")
try:
    import peft
    print("Success.")
except ImportError as e:
    print(f"Failed: {e}")

print("Importing datasets...")
try:
    import datasets
    print("Success.")
except ImportError as e:
    print(f"Failed: {e}")

print("Importing trl...")
try:
    import trl
    print("Success.")
except ImportError as e:
    print(f"Failed: {e}")
