# Complete Financial Training Dataset - Merging all sources

import json

# Import all training data
from financial_training_data import financial_training_data
from bank_loan_data import bank_loan_training_data

# Combine all datasets
complete_training_data = financial_training_data + bank_loan_training_data

# Add more specific bank product data
additional_bank_data = [
    {
        "instruction": "Provide information about specific loan schemes",
        "input": "Tell me about SBI Shaurya home loan for defense personnel",
        "output": """**SBI Shaurya Home Loan - For Defense Personnel:**

**Eligibility:**
- Indian Army personnel
- Indian Navy personnel
- Indian Air Force personnel
- Paramilitary forces
- Ex-servicemen (within 1 year of retirement)

**Interest Rate:**
- **Special Rate:** 8.25% p.a. (0.25% lower than regular)
- **Floating Rate:** Linked to RLLR

**Loan Amount:**
- Minimum: ₹1 lakh
- Maximum: ₹7.5 crore (metro), ₹5 crore (non-metro)
- Based on: Repayment capacity

**Tenure:**
- Maximum: 30 years
- Or up to age 70, whichever is earlier

**Processing Fees:**
- **Waived off** for defense personnel
- Zero processing charges

**Key Features:**
1. **Lower Interest Rate:** 8.25% vs 8.50% regular
2. **No Processing Fee:** Save ₹10,000-35,000
3. **Higher Loan Amount:** Up to ₹7.5 crore
4. **Flexible Repayment:** Adjust with postings
5. **Quick Processing:** 7-10 days approval

**Documents Required:**
- Identity Card from Armed Forces
- Last 6 months salary slips
- Bank statement (6 months)
- Property documents
- PAN, Aadhaar

**Special Benefits:**
- Transfer facility during postings
- EMI holiday during field postings
- Life insurance coverage
- Accidental insurance included

**EMI Calculation:**
Loan: ₹50 lakh | Rate: 8.25% | Tenure: 20 years
**Monthly EMI:** ₹42,857
**Total Interest:** ₹52,85,680
**Savings vs Regular:** ₹1,28,160 over 20 years

**Tax Benefits:**
- Principal: ₹1.5 lakh (Section 80C)
- Interest: ₹2 lakh (Section 24)
- Total: ₹3.5 lakh per year"""
    },
    {
        "instruction": "Explain government loan schemes",
        "input": "What is PMAY and how does it help in home loans?",
        "output": """**Pradhan Mantri Awas Yojana (PMAY) - Credit Linked Subsidy Scheme:**

**What is PMAY?**
Government scheme to provide affordable housing for all by providing interest subsidy on home loans.

**Eligibility Categories:**

**1. EWS (Economically Weaker Section):**
- Annual Income: Up to ₹3 lakh
- Subsidy: 6.50% on loan up to ₹6 lakh
- Max Subsidy: ₹2,67,280
- Carpet Area: Up to 30 sq.m (323 sq.ft)

**2. LIG (Lower Income Group):**
- Annual Income: ₹3-6 lakh
- Subsidy: 6.50% on loan up to ₹6 lakh
- Max Subsidy: ₹2,67,280
- Carpet Area: Up to 60 sq.m (646 sq.ft)

**3. MIG-I (Middle Income Group-I):**
- Annual Income: ₹6-12 lakh
- Subsidy: 4% on loan up to ₹9 lakh
- Max Subsidy: ₹2,35,068
- Carpet Area: Up to 160 sq.m (1722 sq.ft)

**4. MIG-II (Middle Income Group-II):**
- Annual Income: ₹12-18 lakh
- Subsidy: 3% on loan up to ₹12 lakh
- Max Subsidy: ₹2,30,156
- Carpet Area: Up to 200 sq.m (2153 sq.ft)

**How Subsidy Works:**

**Example - MIG-I:**
- Loan Amount: ₹25 lakh
- Interest Rate: 8.50% p.a.
- Tenure: 20 years

**Without PMAY:**
- EMI: ₹21,695
- Total Interest: ₹27,06,800

**With PMAY (4% subsidy on ₹9 lakh):**
- Effective Rate: 4.50% on ₹9 lakh, 8.50% on ₹16 lakh
- EMI: ₹19,460
- Total Interest: ₹24,71,732
- **Savings: ₹2,35,068**

**Eligibility Criteria:**
- First-time home buyer
- No pucca house in family name
- Not availed central government housing scheme
- Annual income within limits
- Property in PMAY approved project

**Documents Required:**
- Income Certificate
- Aadhaar Card
- PAN Card
- Property documents
- Bank statements
- Salary slips/ITR

**Application Process:**
1. Check eligibility on PMAY website
2. Apply through bank/HFC
3. Submit documents
4. Get loan approval
5. Subsidy credited upfront

**Participating Banks:**
- SBI, HDFC, ICICI, Axis, PNB
- All major banks and HFCs
- 50+ lenders

**Key Points:**
- Subsidy given upfront (reduces principal)
- One-time benefit per family
- Valid till scheme ends
- Can be combined with state schemes

**PMAY vs Regular Loan (₹25 lakh, 20 years):**

| Aspect | Regular | PMAY (MIG-I) |
|--------|---------|--------------|
| Rate | 8.50% | 4.50% on ₹9L |
| EMI | ₹21,695 | ₹19,460 |
| Interest | ₹27,06,800 | ₹24,71,732 |
| **Savings** | - | **₹2,35,068** |"""
    }
]

complete_training_data.extend(additional_bank_data)

# Save to JSON
with open('complete_financial_training.json', 'w', encoding='utf-8') as f:
    json.dump(complete_training_data, f, ensure_ascii=False, indent=2)

print(f"✅ Created complete training dataset!")
print(f"📊 Total training examples: {len(complete_training_data)}")
print(f"💾 Saved to: complete_financial_training.json")
print(f"\n📋 Dataset breakdown:")
print(f"   - General financial advice: 20 examples")
print(f"   - Detailed bank loan data: 6 examples")
print(f"   - Government schemes: 2 examples")
print(f"   - Total: {len(complete_training_data)} examples")
