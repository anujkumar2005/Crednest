# Financial Training Dataset for CredNest AI
# Comprehensive finance and money-related Q&A pairs

financial_training_data = [
    # ==================== EMI & LOAN CALCULATIONS ====================
    {
        "instruction": "Calculate EMI for a loan",
        "input": "Calculate EMI for ₹5 lakh loan at 10% interest for 5 years",
        "output": "For a loan of ₹5,00,000 at 10% annual interest for 5 years (60 months):\n\n**Monthly EMI:** ₹10,624\n**Total Amount Payable:** ₹6,37,440\n**Total Interest:** ₹1,37,440\n\n**Formula:** EMI = P × r × (1 + r)^n / ((1 + r)^n - 1)\nWhere:\n- P = Principal (₹5,00,000)\n- r = Monthly interest rate (10%/12 = 0.00833)\n- n = Number of months (60)\n\n**Breakdown:**\nYear 1: Interest ₹48,456 | Principal ₹79,032\nYear 5: Interest ₹11,234 | Principal ₹1,16,254"
    },
    {
        "instruction": "Calculate EMI for a loan",
        "input": "What will be my EMI for ₹20 lakh home loan at 8.5% for 20 years?",
        "output": "For a home loan of ₹20,00,000 at 8.5% annual interest for 20 years (240 months):\n\n**Monthly EMI:** ₹17,252\n**Total Amount Payable:** ₹41,40,480\n**Total Interest:** ₹21,40,480\n\n**Tax Benefits:**\n- Principal repayment: Up to ₹1.5 lakh (Section 80C)\n- Interest payment: Up to ₹2 lakh (Section 24)\n- Total tax saving: Up to ₹3.5 lakh per year\n\n**Recommendation:** With tax benefits, effective interest rate reduces to ~6.5%"
    },
    {
        "instruction": "Calculate EMI for a loan",
        "input": "Car loan EMI for ₹8 lakh at 9% for 7 years",
        "output": "For a car loan of ₹8,00,000 at 9% annual interest for 7 years (84 months):\n\n**Monthly EMI:** ₹12,824\n**Total Amount Payable:** ₹10,77,216\n**Total Interest:** ₹2,77,216\n\n**Comparison with shorter tenure:**\n- 5 years: EMI ₹16,583 | Total Interest ₹1,94,980 (Save ₹82,236)\n- 3 years: EMI ₹25,426 | Total Interest ₹1,15,336 (Save ₹1,61,880)\n\n**Tip:** Shorter tenure = Lower total interest but higher EMI"
    },

    # ==================== LOAN ELIGIBILITY ====================
    {
        "instruction": "Check loan eligibility",
        "input": "Am I eligible for ₹10 lakh loan with ₹50,000 monthly income?",
        "output": "**Loan Eligibility Analysis:**\n\nYour Monthly Income: ₹50,000\nRequested Loan: ₹10,00,000\n\n**Maximum Eligible Loan:** ₹30,00,000 (60× monthly income)\n\n**Status:** ✅ **ELIGIBLE**\n\n**Detailed Analysis:**\n- Income-to-EMI ratio: 40% (Recommended: <50%)\n- Estimated EMI: ₹20,000 (at 10% for 5 years)\n- Remaining income: ₹30,000\n\n**Requirements:**\n- CIBIL Score: 750+ (for best rates)\n- Employment: 2+ years\n- Age: 21-60 years\n- Documents: Salary slips, bank statements, ID proof\n\n**Recommendation:** You're well within limits. Apply with CIBIL 750+ for 8-9% interest rate."
    },
    {
        "instruction": "Check loan eligibility",
        "input": "Can I get ₹50 lakh home loan with ₹1 lakh monthly salary?",
        "output": "**Home Loan Eligibility Analysis:**\n\nYour Monthly Income: ₹1,00,000\nRequested Loan: ₹50,00,000\n\n**Maximum Eligible Loan:** ₹60,00,000 (60× monthly income)\n\n**Status:** ✅ **ELIGIBLE**\n\n**EMI Calculation (at 8.5% for 20 years):**\n- Monthly EMI: ₹43,130\n- EMI-to-Income Ratio: 43.13% ✅ (Under 50% limit)\n\n**Additional Factors:**\n- Existing EMIs: Should be <₹20,000\n- CIBIL Score: 750+ required\n- Down Payment: ₹10-15 lakh (20-30%)\n- Property Value: ₹60-65 lakh\n\n**Tax Benefits:**\n- Save up to ₹3.5 lakh/year in taxes\n- Effective interest: ~6.5% after tax\n\n**Recommendation:** Excellent eligibility! Negotiate for 8-8.5% rate with good CIBIL score."
    },

    # ==================== BUDGETING & SAVING ====================
    {
        "instruction": "Provide budgeting advice",
        "input": "How should I plan my monthly budget with ₹60,000 salary?",
        "output": "**Monthly Budget Plan for ₹60,000 Income:**\n\n**50-30-20 Rule Breakdown:**\n\n**1. Needs (50% = ₹30,000)**\n- Rent/EMI: ₹12,000-15,000\n- Groceries: ₹6,000-8,000\n- Utilities: ₹2,000-3,000\n- Transport: ₹3,000-4,000\n- Insurance: ₹2,000-3,000\n\n**2. Wants (30% = ₹18,000)**\n- Dining out: ₹4,000-5,000\n- Entertainment: ₹3,000-4,000\n- Shopping: ₹5,000-6,000\n- Hobbies: ₹3,000-4,000\n- Subscriptions: ₹1,000-2,000\n\n**3. Savings (20% = ₹12,000)**\n- Emergency Fund: ₹4,000\n- SIP/Mutual Funds: ₹5,000\n- PPF/FD: ₹2,000\n- Gold/Other: ₹1,000\n\n**Pro Tips:**\n- Build 6-month emergency fund first (₹3.6 lakh)\n- Automate savings on salary day\n- Track expenses daily\n- Review and adjust monthly"
    },
    {
        "instruction": "Provide financial tips",
        "input": "Give me tips for saving money effectively",
        "output": "**Top 15 Money-Saving Tips:**\n\n**Immediate Actions:**\n1. **50-30-20 Rule:** 50% needs, 30% wants, 20% savings\n2. **Automate Savings:** Transfer to savings account on salary day\n3. **Track Expenses:** Use apps like CredNest AI, Money Manager\n4. **Cancel Subscriptions:** Remove unused Netflix, Spotify, gym\n5. **Cook at Home:** Save ₹5,000-10,000/month\n\n**Smart Shopping:**\n6. **Compare Prices:** Use price comparison websites\n7. **Use Cashback:** Credit cards with 2-5% cashback\n8. **Buy Generic:** Generic brands save 30-40%\n9. **Wait 24 Hours:** Avoid impulse purchases\n10. **Seasonal Sales:** Buy during festive sales\n\n**Long-term Strategies:**\n11. **Emergency Fund:** Build 6 months expenses\n12. **Invest Early:** Start SIP from ₹500/month\n13. **Reduce Debt:** Pay high-interest loans first\n14. **Negotiate Bills:** Reduce insurance, phone bills\n15. **Side Income:** Freelance, part-time work\n\n**Expected Savings:** ₹10,000-20,000/month"
    },
    {
        "instruction": "Provide budgeting advice",
        "input": "How to create an emergency fund?",
        "output": "**Emergency Fund Creation Guide:**\n\n**What is Emergency Fund?**\nMoney set aside for unexpected expenses like:\n- Job loss\n- Medical emergencies\n- Home/car repairs\n- Family emergencies\n\n**How Much to Save:**\n- **Minimum:** 3 months of expenses\n- **Recommended:** 6 months of expenses\n- **Ideal:** 12 months of expenses\n\n**Example Calculation:**\nMonthly Expenses: ₹40,000\n- 3 months: ₹1,20,000\n- 6 months: ₹2,40,000\n- 12 months: ₹4,80,000\n\n**How to Build:**\n1. **Start Small:** ₹5,000-10,000/month\n2. **Automate:** Set up auto-transfer\n3. **Use Windfalls:** Bonus, tax refund\n4. **Cut Expenses:** Reduce wants temporarily\n5. **Timeline:** 12-24 months to build fully\n\n**Where to Keep:**\n- Savings Account (4% interest)\n- Liquid Mutual Funds (6-7% interest)\n- Fixed Deposits (6-7% interest)\n\n**Don't Use For:**\n- Vacations\n- Shopping\n- Investments\n- Planned expenses\n\n**Use Only For:** True emergencies!"
    },

    # ==================== INVESTMENTS ====================
    {
        "instruction": "Explain investment options",
        "input": "What are the best investment options in India for beginners?",
        "output": "**Best Investment Options for Beginners in India:**\n\n**1. Mutual Funds (SIP)**\n- **Returns:** 12-15% p.a.\n- **Risk:** Medium to High\n- **Min Investment:** ₹500/month\n- **Best For:** Long-term wealth (5+ years)\n- **Tax:** LTCG 10% above ₹1 lakh\n- **Recommendation:** Start with index funds\n\n**2. Public Provident Fund (PPF)**\n- **Returns:** 7.1% p.a. (tax-free)\n- **Risk:** Zero (Government backed)\n- **Min Investment:** ₹500/year\n- **Lock-in:** 15 years\n- **Tax:** EEE (Exempt-Exempt-Exempt)\n- **Best For:** Retirement planning\n\n**3. Fixed Deposits (FD)**\n- **Returns:** 6-7.5% p.a.\n- **Risk:** Very Low\n- **Min Investment:** ₹1,000\n- **Tenure:** 7 days to 10 years\n- **Tax:** Taxable as per slab\n- **Best For:** Short-term goals (1-3 years)\n\n**4. National Pension System (NPS)**\n- **Returns:** 10-12% p.a.\n- **Risk:** Medium\n- **Min Investment:** ₹500/month\n- **Lock-in:** Till 60 years\n- **Tax:** Additional ₹50,000 deduction (80CCD)\n- **Best For:** Retirement corpus\n\n**5. Gold (Digital/ETF)**\n- **Returns:** 8-10% p.a.\n- **Risk:** Medium\n- **Min Investment:** ₹100\n- **Best For:** Portfolio diversification\n- **Tax:** LTCG 20% with indexation\n\n**Beginner's Portfolio:**\n- 40% Equity Mutual Funds (SIP)\n- 30% PPF/NPS\n- 20% FD/Debt Funds\n- 10% Gold\n\n**Start with:** ₹5,000-10,000/month total"
    },
    {
        "instruction": "Calculate SIP returns",
        "input": "How much will I get if I invest ₹5,000 monthly in SIP for 10 years?",
        "output": "**SIP Investment Calculation:**\n\nMonthly Investment: ₹5,000\nTenure: 10 years (120 months)\nExpected Return: 12% p.a.\n\n**Results:**\n- **Total Invested:** ₹6,00,000\n- **Expected Returns:** ₹5,52,018\n- **Maturity Value:** ₹11,52,018\n\n**Year-wise Growth:**\n- Year 1: ₹61,780\n- Year 5: ₹4,12,432\n- Year 10: ₹11,52,018\n\n**Comparison with Different Returns:**\n- 10% return: ₹10,23,391 (₹4,23,391 profit)\n- 12% return: ₹11,52,018 (₹5,52,018 profit)\n- 15% return: ₹13,76,243 (₹7,76,243 profit)\n\n**Power of Compounding:**\nIf you continue for 20 years:\n- Total Invested: ₹12,00,000\n- Maturity Value: ₹49,95,740\n- Profit: ₹37,95,740 (316% returns!)\n\n**Tax Implications:**\n- LTCG: 10% on gains above ₹1 lakh/year\n- Estimated tax: ₹45,000-50,000 (on ₹5.5 lakh profit)\n\n**Recommendation:** Start SIP today! Every year delayed = ₹2-3 lakh less corpus"
    },
    {
        "instruction": "Compare investment options",
        "input": "Should I invest in FD or mutual funds?",
        "output": "**FD vs Mutual Funds Comparison:**\n\n**Fixed Deposit (FD):**\n✅ **Pros:**\n- Guaranteed returns (6-7.5%)\n- Zero risk\n- Capital protection\n- Easy to understand\n- Premature withdrawal allowed\n\n❌ **Cons:**\n- Lower returns\n- Taxable interest\n- Doesn't beat inflation\n- No wealth creation\n\n**Mutual Funds (Equity):**\n✅ **Pros:**\n- Higher returns (12-15%)\n- Beats inflation\n- Wealth creation\n- Tax efficient (LTCG)\n- Professional management\n- Liquidity\n\n❌ **Cons:**\n- Market risk\n- Returns not guaranteed\n- Requires patience\n- Can be volatile\n\n**Example: ₹10,000/month for 10 years**\n\n**FD (7% return):**\n- Invested: ₹12,00,000\n- Maturity: ₹17,40,000\n- Profit: ₹5,40,000\n- Tax: ~₹1,62,000 (30% slab)\n- Net: ₹15,78,000\n\n**Mutual Fund (12% return):**\n- Invested: ₹12,00,000\n- Maturity: ₹23,04,000\n- Profit: ₹11,04,000\n- Tax: ~₹1,00,000 (LTCG)\n- Net: ₹22,04,000\n\n**Difference:** ₹6,26,000 more with mutual funds!\n\n**Recommendation:**\n- **Short-term (1-3 years):** FD\n- **Long-term (5+ years):** Mutual Funds\n- **Balanced:** 70% MF + 30% FD"
    },

    # ==================== TAX PLANNING ====================
    {
        "instruction": "Explain tax saving options",
        "input": "How can I save tax under Section 80C?",
        "output": "**Section 80C Tax Saving Guide:**\n\n**Maximum Deduction:** ₹1,50,000 per year\n\n**Investment Options:**\n\n**1. ELSS Mutual Funds** ⭐ Recommended\n- Lock-in: 3 years (shortest)\n- Returns: 12-15% p.a.\n- Tax: LTCG 10% above ₹1 lakh\n- Best for: Wealth creation\n\n**2. Public Provident Fund (PPF)**\n- Lock-in: 15 years\n- Returns: 7.1% p.a. (tax-free)\n- Best for: Retirement\n\n**3. National Savings Certificate (NSC)**\n- Lock-in: 5 years\n- Returns: 7% p.a.\n- Best for: Conservative investors\n\n**4. Life Insurance Premium**\n- Term insurance: ₹50,000/year\n- Tax saving + protection\n\n**5. Home Loan Principal**\n- Up to ₹1.5 lakh\n- Reduces taxable income\n\n**6. Sukanya Samriddhi Yojana**\n- For girl child\n- Returns: 8% p.a. (tax-free)\n- Lock-in: 21 years\n\n**7. Fixed Deposit (5-year)**\n- Returns: 6.5-7% p.a.\n- Safe option\n\n**8. Employee Provident Fund (EPF)**\n- Auto-deducted from salary\n- Returns: 8.15% p.a.\n\n**Tax Saving Calculation:**\nInvestment: ₹1,50,000\nTax Slab: 30%\n**Tax Saved:** ₹46,800 + cess\n\n**Recommended Split:**\n- ELSS: ₹60,000 (40%)\n- PPF: ₹50,000 (33%)\n- Life Insurance: ₹20,000 (13%)\n- Home Loan: ₹20,000 (13%)"
    },
    {
        "instruction": "Calculate income tax",
        "input": "What will be my tax on ₹10 lakh annual income?",
        "output": "**Income Tax Calculation for ₹10,00,000:**\n\n**New Tax Regime (FY 2024-25):**\n- Up to ₹3 lakh: Nil\n- ₹3-7 lakh: 5% = ₹20,000\n- ₹7-10 lakh: 10% = ₹30,000\n- ₹10-12 lakh: 15% = Nil\n- ₹12-15 lakh: 20% = Nil\n\n**Total Tax:** ₹50,000\n**Cess (4%):** ₹2,000\n**Total Payable:** ₹52,000\n**Monthly TDS:** ₹4,333\n\n**Old Tax Regime (with deductions):**\n- Up to ₹2.5 lakh: Nil\n- ₹2.5-5 lakh: 5% = ₹12,500\n- ₹5-10 lakh: 20% = ₹1,00,000\n\n**Gross Tax:** ₹1,12,500\n\n**Deductions:**\n- 80C: ₹1,50,000 (saves ₹30,000)\n- 80D: ₹25,000 (saves ₹5,000)\n- HRA: ₹1,00,000 (saves ₹20,000)\n- Standard Deduction: ₹50,000 (saves ₹10,000)\n\n**Tax After Deductions:** ₹47,500\n**Cess (4%):** ₹1,900\n**Total Payable:** ₹49,400\n\n**Comparison:**\n- New Regime: ₹52,000\n- Old Regime: ₹49,400\n\n**Recommendation:** Old regime if you have investments, New regime if no deductions\n\n**Take-home Salary:**\n- Gross: ₹10,00,000\n- Tax: ₹49,400\n- PF: ₹21,600\n- **Net:** ₹9,29,000/year (₹77,417/month)"
    },

    # ==================== CREDIT SCORE ====================
    {
        "instruction": "Explain credit score",
        "input": "How can I improve my CIBIL score?",
        "output": "**CIBIL Score Improvement Guide:**\n\n**What is CIBIL Score?**\n- Range: 300-900\n- Good: 750+\n- Excellent: 800+\n- Affects: Loan approval & interest rates\n\n**10 Ways to Improve:**\n\n**1. Pay Bills on Time** (35% weightage)\n- Credit card bills before due date\n- EMIs on time\n- Set auto-pay\n\n**2. Keep Credit Utilization Low** (30% weightage)\n- Use <30% of credit limit\n- Example: ₹1 lakh limit = Use max ₹30,000\n\n**3. Maintain Old Accounts** (15% weightage)\n- Don't close old credit cards\n- Longer credit history = better score\n\n**4. Limit Hard Inquiries** (10% weightage)\n- Don't apply for multiple loans\n- Space out applications by 6 months\n\n**5. Mix of Credit** (10% weightage)\n- Have both secured (home) & unsecured (credit card)\n- Balanced portfolio\n\n**6. Check Report Regularly**\n- Free annual report from CIBIL\n- Dispute errors immediately\n\n**7. Pay More Than Minimum**\n- Pay full credit card balance\n- Avoid revolving credit\n\n**8. Don't Max Out Cards**\n- Keep buffer of 50%\n- Better to have 2 cards with low usage\n\n**9. Become Authorized User**\n- Add to family member's good account\n\n**10. Settle Dues**\n- Clear all outstanding dues\n- Avoid settlements (marks as negative)\n\n**Timeline:**\n- 3 months: +20-30 points\n- 6 months: +50-70 points\n- 12 months: +100-150 points\n\n**Score Impact on Loans:**\n- 750-900: 8-9% interest\n- 700-749: 9-10% interest\n- 650-699: 10-12% interest\n- <650: Loan rejection or 12%+ interest\n\n**Example:** On ₹20 lakh loan\n- 750 score (8.5%): EMI ₹17,252\n- 650 score (11%): EMI ₹20,647\n- **Difference:** ₹3,395/month = ₹8.15 lakh over 20 years!"
    },

    # ==================== INSURANCE ====================
    {
        "instruction": "Explain insurance types",
        "input": "What type of insurance do I need?",
        "output": "**Essential Insurance Types for Indians:**\n\n**1. Term Life Insurance** 🔴 MUST HAVE\n- **Coverage:** 10-15× annual income\n- **Example:** ₹50 lakh income = ₹5-7.5 crore cover\n- **Premium:** ₹10,000-20,000/year (₹1 crore cover)\n- **Who Needs:** Anyone with dependents\n- **Recommendation:** Buy before 30 for low premium\n\n**2. Health Insurance** 🔴 MUST HAVE\n- **Coverage:** ₹5-10 lakh minimum\n- **Family Floater:** ₹10-15 lakh\n- **Premium:** ₹15,000-30,000/year\n- **Who Needs:** Everyone\n- **Tip:** Employer insurance not enough\n\n**3. Accidental Insurance** 🟡 RECOMMENDED\n- **Coverage:** ₹50 lakh - ₹1 crore\n- **Premium:** ₹500-1,000/year\n- **Who Needs:** Working professionals\n- **Benefit:** Very cheap, high coverage\n\n**4. Critical Illness** 🟡 RECOMMENDED\n- **Coverage:** ₹25-50 lakh\n- **Premium:** ₹8,000-15,000/year\n- **Covers:** Cancer, heart attack, stroke\n- **Who Needs:** 30+ age, family history\n\n**5. Motor Insurance** 🔴 MUST HAVE (Legal)\n- **Third Party:** ₹2,000-5,000/year\n- **Comprehensive:** ₹8,000-20,000/year\n- **Who Needs:** All vehicle owners\n\n**6. Home Insurance** 🟢 OPTIONAL\n- **Coverage:** ₹10-50 lakh\n- **Premium:** ₹3,000-10,000/year\n- **Covers:** Fire, theft, natural disasters\n\n**Priority Order:**\n1. Health Insurance (₹10 lakh)\n2. Term Life (₹1 crore)\n3. Accidental (₹50 lakh)\n4. Motor (Comprehensive)\n5. Critical Illness\n6. Home Insurance\n\n**Total Annual Premium:** ₹40,000-60,000\n\n**Tax Benefits:**\n- Health: ₹25,000 deduction (80D)\n- Life: ₹1.5 lakh deduction (80C)\n- **Total Tax Saving:** ₹52,500 (30% slab)"
    },

    # ==================== RETIREMENT PLANNING ====================
    {
        "instruction": "Plan for retirement",
        "input": "How much should I save for retirement?",
        "output": "**Retirement Planning Guide:**\n\n**Assumptions:**\n- Current Age: 30 years\n- Retirement Age: 60 years\n- Life Expectancy: 85 years\n- Current Monthly Expenses: ₹50,000\n- Inflation: 6% p.a.\n\n**Step 1: Calculate Future Expenses**\nMonthly expenses at 60: ₹2,87,175\nYearly expenses: ₹34,46,100\n\n**Step 2: Corpus Required**\nFor 25 years post-retirement: **₹8.6 Crore**\n\n**Step 3: How to Build ₹8.6 Crore**\n\n**Option 1: SIP in Equity Mutual Funds**\n- Monthly SIP: ₹25,000\n- Tenure: 30 years\n- Expected Return: 12% p.a.\n- **Maturity:** ₹8.8 Crore ✅\n\n**Option 2: Mixed Portfolio**\n- Equity MF: ₹15,000 (60%)\n- PPF: ₹7,000 (28%)\n- NPS: ₹3,000 (12%)\n- **Total:** ₹25,000/month\n- **Maturity:** ₹8.5 Crore ✅\n\n**Option 3: Conservative**\n- PPF: ₹12,500\n- NPS: ₹7,500\n- FD: ₹5,000\n- **Total:** ₹25,000/month\n- **Maturity:** ₹6.2 Crore ⚠️ (Shortfall)\n\n**Retirement Income Sources:**\n1. **Corpus:** ₹8.6 crore\n2. **EPF:** ₹1.5-2 crore\n3. **NPS:** ₹1-1.5 crore\n4. **Rental Income:** ₹30,000-50,000/month\n5. **Pension:** ₹20,000-30,000/month\n\n**Monthly Income at Retirement:**\n- Corpus withdrawal (4% rule): ₹2,87,000\n- Pension: ₹25,000\n- Rental: ₹40,000\n- **Total:** ₹3,52,000/month ✅\n\n**Action Plan:**\n- Age 30-40: Aggressive (80% equity)\n- Age 40-50: Balanced (60% equity)\n- Age 50-60: Conservative (40% equity)\n\n**Start NOW:** Delaying by 5 years = ₹2 crore less corpus!"
    },

    # ==================== REAL ESTATE ====================
    {
        "instruction": "Advise on property purchase",
        "input": "Should I buy a house or rent?",
        "output": "**Buy vs Rent Analysis:**\n\n**Scenario:** ₹50 lakh property in Tier-1 city\n\n**BUYING:**\n**Initial Costs:**\n- Property: ₹50,00,000\n- Down Payment (20%): ₹10,00,000\n- Loan: ₹40,00,000\n- Registration (7%): ₹3,50,000\n- **Total Initial:** ₹13,50,000\n\n**Monthly Costs:**\n- EMI (8.5%, 20 years): ₹34,602\n- Maintenance: ₹3,000\n- Property Tax: ₹1,000\n- **Total:** ₹38,602/month\n\n**Benefits:**\n- Tax saving: ₹3.5 lakh/year\n- Property appreciation: 5-7% p.a.\n- Own asset\n- No rent increase\n\n**RENTING:**\n**Monthly Costs:**\n- Rent: ₹15,000\n- Maintenance: ₹2,000\n- **Total:** ₹17,000/month\n\n**Investment Alternative:**\n- Invest ₹13.5 lakh + ₹21,602/month\n- In mutual funds (12% return)\n- After 20 years: ₹2.1 crore\n\n**20-Year Comparison:**\n\n**Buying:**\n- Total Paid: ₹83 lakh (EMI) + ₹13.5 lakh (initial)\n- Property Value: ₹1.8 crore (7% appreciation)\n- **Net Worth:** ₹1.8 crore - ₹96.5 lakh = **₹83.5 lakh**\n\n**Renting + Investing:**\n- Total Rent Paid: ₹51 lakh\n- Investment Corpus: ₹2.1 crore\n- **Net Worth:** ₹2.1 crore - ₹51 lakh = **₹1.59 crore**\n\n**Verdict:**\n✅ **Buy if:**\n- Staying >7 years\n- Property in prime location\n- Rental yield >3%\n- Emotional value\n\n✅ **Rent if:**\n- Job requires mobility\n- Property overpriced\n- Can invest disciplined\n- Rental yield <2%\n\n**Recommendation:** In current market (2024), renting + investing often better financially, but buying gives stability and forced savings."
    },

    # ==================== FINANCIAL MISTAKES ====================
    {
        "instruction": "Explain common financial mistakes",
        "input": "What financial mistakes should I avoid?",
        "output": "**Top 20 Financial Mistakes to Avoid:**\n\n**1. No Emergency Fund** 🔴\n- Impact: Debt during crisis\n- Solution: Build 6-month expenses\n\n**2. Not Starting Early** 🔴\n- Impact: Miss compounding benefits\n- Solution: Start SIP from first salary\n\n**3. Only Saving, Not Investing** 🔴\n- Impact: Money loses value to inflation\n- Solution: 70% invest, 30% save\n\n**4. Buying Insurance as Investment** 🔴\n- Impact: Low returns, high premium\n- Solution: Term insurance + separate investments\n\n**5. Credit Card Debt** 🔴\n- Impact: 36-42% interest\n- Solution: Pay full balance monthly\n\n**6. No Health Insurance** 🔴\n- Impact: Medical emergency = bankruptcy\n- Solution: ₹10 lakh family floater\n\n**7. Lifestyle Inflation** 🟡\n- Impact: No savings despite high income\n- Solution: Save 50% of every raise\n\n**8. Not Tracking Expenses** 🟡\n- Impact: Money disappears\n- Solution: Use budgeting apps\n\n**9. Too Many Loans** 🟡\n- Impact: EMI burden >50% income\n- Solution: Keep EMI <40% income\n\n**10. Ignoring Tax Planning** 🟡\n- Impact: Pay unnecessary tax\n- Solution: Use 80C, 80D deductions\n\n**11. Following Stock Tips** 🟡\n- Impact: Losses from speculation\n- Solution: Invest in index funds\n\n**12. No Retirement Planning** 🔴\n- Impact: Dependent on children\n- Solution: Start NPS/PPF early\n\n**13. Buying New Car** 🟢\n- Impact: Depreciates 20% immediately\n- Solution: Buy 2-3 year old car\n\n**14. Not Reading Fine Print** 🟡\n- Impact: Hidden charges, penalties\n- Solution: Read all documents\n\n**15. Emotional Investing** 🟡\n- Impact: Buy high, sell low\n- Solution: Stick to SIP, ignore market\n\n**16. Too Much Real Estate** 🟢\n- Impact: Illiquid, low returns\n- Solution: Max 40% in real estate\n\n**17. No Will/Nomination** 🟡\n- Impact: Family disputes\n- Solution: Make will, add nominees\n\n**18. Lending to Friends** 🟢\n- Impact: Lose money + friendship\n- Solution: Gift if you can afford\n\n**19. Not Diversifying** 🟡\n- Impact: All eggs in one basket\n- Solution: Spread across assets\n\n**20. Ignoring Inflation** 🟡\n- Impact: Future goals underfunded\n- Solution: Assume 6% inflation\n\n**Cost of Mistakes:**\nAvoiding these can save ₹50 lakh - ₹1 crore over lifetime!"
    },

    # ==================== INDIAN FINANCIAL REGULATIONS ====================
    {
        "instruction": "Explain financial regulations",
        "input": "What are the important financial rules in India?",
        "output": "**Key Financial Regulations in India (2024):**\n\n**1. Income Tax Rules**\n- Tax filing deadline: July 31\n- PAN mandatory for transactions >₹50,000\n- TDS on salary, interest, rent\n- Advance tax if liability >₹10,000\n\n**2. GST Rules**\n- 5%, 12%, 18%, 28% slabs\n- Registration mandatory if turnover >₹40 lakh\n- Monthly/quarterly returns\n\n**3. Banking Rules**\n- KYC mandatory for all accounts\n- Cash deposit >₹50,000/day needs PAN\n- Cash withdrawal >₹1 crore/year = TDS\n- Minimum balance requirements\n\n**4. Investment Limits**\n- PPF: Max ₹1.5 lakh/year\n- NPS: No limit (tax benefit ₹2 lakh)\n- ELSS: No limit (80C benefit ₹1.5 lakh)\n- Sukanya: Max ₹1.5 lakh/year\n\n**5. Loan Rules**\n- Home loan: Max 80% LTV\n- Personal loan: Max ₹40 lakh\n- Credit card: Min 5% payment\n- Foreclosure: No charges after 6 months\n\n**6. Insurance Rules**\n- Motor insurance: Mandatory\n- Health portability: After 1 year\n- Claim settlement: Within 30 days\n- Free look period: 15-30 days\n\n**7. Property Rules**\n- Stamp duty: 5-7% (state-wise)\n- Registration: 1% of value\n- Capital gains: LTCG 20% (>2 years)\n- TDS: 1% on sale >₹50 lakh\n\n**8. Digital Payment Rules**\n- UPI: Free up to ₹1 lakh/transaction\n- NEFT/RTGS: Free\n- Cash transactions >₹2 lakh: Prohibited\n- Digital payments: No charges\n\n**9. Senior Citizen Benefits**\n- Higher FD rates (+0.5%)\n- Tax exemption: ₹3 lakh (old regime)\n- Health deduction: ₹50,000 (80D)\n- SCSS: 8.2% interest\n\n**10. Penalties**\n- Late tax filing: ₹5,000-10,000\n- Wrong PAN: Transaction rejected\n- Loan default: CIBIL impact\n- Insurance lapse: No claim\n\n**Recent Changes (2024):**\n- New tax regime default\n- Standard deduction: ₹50,000\n- Leave encashment: ₹25 lakh exempt\n- TDS on crypto: 1%\n\n**Compliance Checklist:**\n✅ File ITR annually\n✅ Update KYC every 2 years\n✅ Link PAN-Aadhaar\n✅ Maintain 6-year tax records\n✅ Declare foreign assets\n✅ Pay advance tax quarterly"
    }
]

# Export to JSON for easy use
import json

with open('financial_training_data.json', 'w', encoding='utf-8') as f:
    json.dump(financial_training_data, f, ensure_ascii=False, indent=2)

print(f"Created {len(financial_training_data)} comprehensive financial training examples!")
print("Saved to: financial_training_data.json")
