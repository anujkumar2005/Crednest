
import torch
import transformers
import tokenizers
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from peft import LoraConfig, prepare_model_for_kbit_training, get_peft_model
from datasets import Dataset
from trl import SFTTrainer
import json
import os

# 1. Check Versions
print("Step 1: Checking Versions...")
print(f"PyTorch: {torch.__version__}")
print(f"Transformers: {transformers.__version__}")
print(f"Tokenizers: {tokenizers.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")

if not torch.cuda.is_available():
    print("❌ CUDA not available. Cannot proceed with 4-bit quantization.")
    exit(1)

# 2. Load Data
print("\nStep 2: Loading Data...")
try:
    with open('server/complete_financial_training.json', 'r', encoding='utf-8') as f:
        training_data = json.load(f)
    print(f"✅ Loaded {len(training_data)} examples")
except Exception as e:
    print(f"❌ Error loading data: {e}")
    exit(1)

def format_instruction(sample):
    return f"""### Instruction:
{sample['instruction']}

### Input:
{sample['input']}

### Response:
{sample['output']}"""

dataset = Dataset.from_list(training_data)
dataset = dataset.map(lambda x: {"text": format_instruction(x)})

# 3. Load Model & Tokenizer
print("\nStep 3: Loading Model & Tokenizer...")
model_name = "mistralai/Mistral-7B-v0.1"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

try:
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    print("✅ Tokenizer loaded")
except Exception as e:
    print(f"❌ Error loading tokenizer: {e}")
    exit(1)

try:
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )
    model = prepare_model_for_kbit_training(model)
    print("✅ Model loaded")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit(1)

# 4. Configure LoRA
print("\nStep 4: Configuring LoRA...")
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
)
model = get_peft_model(model, peft_config)

# 5. Initialize Trainer (Dry Run)
print("\nStep 5: Initializing Trainer (Dry Run)...")
training_args = TrainingArguments(
    output_dir="./crednest-ai-model-verify",
    num_train_epochs=1,
    max_steps=1, # Only run 1 step to verify
    per_device_train_batch_size=1,
    gradient_accumulation_steps=1,
    optim="paged_adamw_8bit",
    logging_steps=1,
    learning_rate=2e-4,
    fp16=True,
    report_to="none",
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    dataset_text_field="text",
    max_seq_length=512,
    tokenizer=tokenizer,
    args=training_args,
)

print("✅ Trainer initialized")

# 6. Run Training Step
print("\nStep 6: Running 1 Training Step...")
try:
    trainer.train()
    print("✅ Training step successful")
except Exception as e:
    print(f"❌ Error during training: {e}")
    exit(1)

print("\n🎉 Verification Complete! The code works.")
