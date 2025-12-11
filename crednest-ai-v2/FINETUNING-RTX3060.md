# 🚀 Fine-tuning for Your RTX 3060 - Step by Step

## ✅ Your System
- **GPU:** RTX 3060 6GB VRAM
- **CPU:** AMD Ryzen 7 5800H
- **RAM:** 16GB
- **Python:** 3.10.0 ✅
- **Training Data:** 27 examples (44KB) ✅

---

## 📦 Step 1: Install Required Packages

Copy and paste these commands **one by one** in PowerShell:

```powershell
# 1. Install PyTorch with CUDA (for RTX 3060)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Wait for this to complete (~2-3 GB download), then:

```powershell
# 2. Install AI training packages
pip install transformers==4.36.0 peft==0.7.1 bitsandbytes==0.41.3 accelerate==0.25.0 datasets==2.15.0 trl==0.7.4 scipy
```

**Note:** Jupyter is already installing in the background!

---

## 🎯 Step 2: Start Jupyter Notebook

After installations complete:

```powershell
cd d:\crednest-ai\crednest-ai-v2
jupyter notebook model-finetuning.ipynb
```

This will open your browser automatically.

---

## 📝 Step 3: Run the Training

In the Jupyter browser window:

1. Click **"Cell"** in the menu
2. Click **"Run All"**
3. Wait 10-15 minutes

You'll see output like:
```
Loading model with 4-bit quantization...
Model loaded successfully!
Training...
Step 10: Loss = 2.45
Step 20: Loss = 1.82
...
✅ Training complete!
```

---

## ⚡ What's Optimized for Your RTX 3060

**Memory Optimizations:**
- ✅ 4-bit quantization (uses ~4GB instead of 14GB)
- ✅ LoRA adapters (trains only 0.1% of parameters)
- ✅ Gradient checkpointing (saves VRAM)
- ✅ Batch size = 1 (minimal memory)
- ✅ Mixed precision FP16

**Expected VRAM Usage:** ~5.5GB (safe for 6GB card)

---

## 🎓 Training Details

**Model:** Mistral-7B (7 billion parameters)
**Method:** LoRA fine-tuning
**Data:** 27 financial examples
**Epochs:** 3
**Time:** 10-15 minutes
**Output:** 4GB model

---

## 📊 What the Model Will Learn

After training, your AI will know:

**Bank-Specific Data:**
- SBI home loans: 8.25-9.65%
- HDFC home loans: 8.60-9.50%
- ICICI personal loans: 10.75-16%
- Axis car loans: 8.75-13%
- PNB education loans: 8.85-10.35%

**Financial Calculations:**
- EMI formulas
- Loan eligibility
- Tax benefits (80C, 80D, 24)
- SIP returns
- PMAY subsidies

**Indian Finance:**
- Government schemes
- Credit score tips
- Investment strategies
- Retirement planning

---

## 🔧 If You Get Errors

**"CUDA not available":**
```powershell
# Install CUDA Toolkit 11.8
# Download from: https://developer.nvidia.com/cuda-11-8-0-download-archive
```

**"Out of memory":**
- Close Chrome and other apps
- The notebook is already optimized for 6GB
- Should not happen with current settings

**"Module not found":**
```powershell
# Reinstall the missing package
pip install <package-name>
```

---

## 🎯 After Training

**Test the model:**
```python
# In Jupyter notebook (last cell)
prompt = "Calculate EMI for ₹5 lakh at 10% for 5 years"
response = generate_response("Calculate EMI", prompt)
print(response)
```

**Expected output:**
```
For a loan of ₹5,00,000 at 10% annual interest for 5 years:

Monthly EMI: ₹10,624
Total Amount: ₹6,37,440
Total Interest: ₹1,37,440

Formula: EMI = P × r × (1 + r)^n / ((1 + r)^n - 1)
```

---

## 🚀 Quick Start Commands

```powershell
# Install everything (run one by one)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers==4.36.0 peft==0.7.1 bitsandbytes==0.41.3 accelerate==0.25.0 datasets==2.15.0 trl==0.7.4 scipy

# Start Jupyter
cd d:\crednest-ai\crednest-ai-v2
jupyter notebook model-finetuning.ipynb

# In Jupyter: Cell → Run All
# Wait 15 minutes
# Done! 🎉
```

---

**Ready to start! Just follow the steps above!** 🚀
