"""
Financial Literacy Tips Tool
"""

def get_financial_tips(topic: str) -> dict:
    """
    Provide financial tips on various topics
    
    Args:
        topic: credit_score, saving, debt_management, investment, budgeting, loan_management
    
    Returns:
        Dictionary with tips and actionable advice
    """
    
    tips_database = {
        "credit_score": {
            "title": "🎯 How to Improve Your Credit Score",
            "current_importance": "Credit score affects loan approval and interest rates. 750+ gets you best deals!",
            "tips": [
                "✓ Pay ALL credit card bills & EMIs on time - even one late payment hurts for 2 years",
                "✓ Keep credit card utilization under 30% of limit (e.g., use max ₹30k on ₹1L limit)",
                "✓ Don't close old credit cards - longer credit history is better",
                "✓ Avoid multiple loan applications in short time - each inquiry reduces score",
                "✓ Check credit report FREE every 6 months on CIBIL/Experian website",
                "✓ Mix of secured (home/car loan) and unsecured (personal/credit card) credit is ideal",
                "✓ Never settle a loan for less than full amount - shows as negative",
                "✓ Keep separate business and personal credit - mixing confuses lenders"
            ],
            "quick_wins": [
                "Pay off credit card balances immediately",
                "Set up auto-pay for all EMIs",
                "Dispute any errors in credit report",
                "Request credit limit increase (don't use it!)"
            ],
            "timeline": "Expect 6-12 months to see significant improvement"
        },
        
        "saving": {
            "title": "💰 Smart Saving Strategies",
            "current_importance": "Build emergency fund = 6 months expenses. Then invest for goals!",
            "tips": [
                "✓ Follow 50-30-20 rule: 50% needs, 30% wants, 20% savings/investments",
                "✓ Automate savings - transfer to separate account on salary day",
                "✓ Emergency fund FIRST - 6 months expenses in liquid form (savings account/liquid fund)",
                "✓ Use high-interest savings accounts (4-7% p.a.) or liquid funds (5-7% p.a.)",
                "✓ Save ALL bonuses, increments, gifts instead of splurging",
                "✓ Track expenses for 30 days - you'll find ₹3000-5000 to cut",
                "✓ Set specific goals with deadlines (₹2L for vacation in 18 months)",
                "✓ Round-up apps that save ₹10-50 per transaction add up!",
                "✓ Cancel unused subscriptions - average person wastes ₹2000/month"
            ],
            "quick_wins": [
                "Open high-interest savings account today",
                "Set up ₹5000 auto-transfer monthly",
                "Cancel 2-3 unused subscriptions",
                "Pack lunch 3 days/week (saves ₹6000/month)"
            ],
            "timeline": "Build ₹1L emergency fund in 12-18 months"
        },
        
        "debt_management": {
            "title": "📉 Effective Debt Repayment",
            "current_importance": "High-interest debt kills wealth building. Pay off ASAP!",
            "tips": [
                "✓ List ALL debts with interest rates - highest rate first!",
                "✓ Pay off credit cards FIRST (18-36% interest is killing you)",
                "✓ Avalanche method: Pay minimum on all, extra on highest interest",
                "✓ Snowball method: Pay smallest debt first for motivation",
                "✓ Never miss minimum payment - ruins credit score",
                "✓ Negotiate with lenders for lower rates or restructuring",
                "✓ Consolidate multiple high-interest debts into single low-interest loan",
                "✓ STOP adding new debt while paying off existing",
                "✓ Use bonuses/windfalls for lump-sum debt payment",
                "✓ Balance transfer credit cards can save 10-15% interest"
            ],
            "quick_wins": [
                "Pay ₹1000 extra on highest interest debt this month",
                "Call credit card company to waive late fees",
                "Stop using credit cards temporarily",
                "Sell unused items to pay down debt"
            ],
            "priority_order": [
                "1. Credit card debt (18-36% interest)",
                "2. Personal loans (10-16% interest)",
                "3. Car loans (8-12% interest)",
                "4. Home loans (8-10% interest) - LAST priority as rate is low"
            ],
            "timeline": "Aim to be debt-free (except home loan) in 2-3 years"
        },
        
        "investment": {
            "title": "📈 Smart Investment Guide",
            "current_importance": "Investing beats inflation and builds wealth. Start NOW!",
            "tips": [
                "✓ Start SIP even with ₹500/month - consistency matters more than amount",
                "✓ Invest in equity mutual funds for long-term (5+ years) wealth",
                "✓ Diversify: 60% equity, 30% debt, 10% gold (adjust based on age)",
                "✓ Never try to time the market - stay invested through ups and downs",
                "✓ Index funds (Nifty 50/Sensex) are safest for beginners",
                "✓ Increase SIP by 10% annually with salary hike",
                "✓ Tax-saving ELSS funds give deduction + market returns",
                "✓ PPF (7.1%) and EPF for guaranteed safe returns",
                "✓ Avoid insurance-investment combos (ULIPs) - poor returns",
                "✓ Real estate only AFTER you have ₹50L+ investable surplus"
            ],
            "quick_wins": [
                "Open demat account today (Zerodha/Groww/ET Money)",
                "Start ₹1000 SIP in Nifty 50 index fund",
                "Max out ELSS for ₹1.5L tax saving",
                "Rebalance portfolio once a year"
            ],
            "returns_expectation": {
                "Equity mutual funds": "12-15% p.a. long-term",
                "Index funds": "10-12% p.a. long-term", 
                "Debt funds": "6-8% p.a.",
                "PPF/EPF": "7-8% p.a. (guaranteed)",
                "FD": "5-7% p.a. (safe but inflation-beating)"
            },
            "timeline": "₹10,000/month SIP @ 12% = ₹1 Crore in 20 years"
        },
        
        "budgeting": {
            "title": "📊 Budget Like a Pro",
            "current_importance": "Budget is GPS for money - shows where it's going!",
            "tips": [
                "✓ 50-30-20 rule: 50% needs (rent, food), 30% wants (fun), 20% savings",
                "✓ Track EVERY expense for 30 days using app (Walnut/ET Money/Excel)",
                "✓ Allocate money at month start, not month end",
                "✓ Envelope system: Cash for each category in envelopes",
                "✓ Needs vs wants: Phone bill is need, Netflix is want",
                "✓ Review budget monthly - adjust based on reality",
                "✓ Build 'fun money' into budget so you don't feel deprived",
                "✓ Plan for annual expenses (insurance, tax) monthly",
                "✓ Reduce 'Lifestyle inflation' when salary increases"
            ],
            "quick_wins": [
                "Download expense tracking app",
                "Categorize last month's spending",
                "Identify 3 areas to cut ₹1000 each",
                "Set up auto-debit for bills"
            ],
            "timeline": "Takes 3 months to get into budgeting rhythm"
        },
        
        "loan_management": {
            "title": "🏦 Smart Loan Management",
            "current_importance": "Good loans (home) build wealth. Bad loans (credit card) destroy it!",
            "tips": [
                "✓ Keep total EMI under 40% of monthly income (all loans combined)",
                "✓ Good debt: Home loan (appreciating asset). Bad debt: Personal loan for vacation",
                "✓ Always compare 3-4 banks before taking loan",
                "✓ Processing fee negotiable - ask for waiver/reduction",
                "✓ Pre-payment whenever you have extra cash - saves huge interest",
                "✓ Read fine print: Pre-payment penalty, late payment fee, loan insurance",
                "✓ Shorter tenure = less interest but higher EMI. Find balance!",
                "✓ Co-applicant improves eligibility and can get lower rate",
                "✓ Check CIBIL score before applying - 750+ gets best rates",
                "✓ Don't take multiple loans in 6 months - looks desperate to lenders"
            ],
            "quick_wins": [
                "Check current loan interest rates - refinance if lower available",
                "Make one part-payment this year",
                "Set up auto-debit to never miss EMI",
                "Opt for shorter tenure if you can afford higher EMI"
            ],
            "red_flags": [
                "EMI >50% of income - financial disaster waiting",
                "Multiple personal loans simultaneously",
                "Using credit card to pay EMI",
                "Missing EMI payments"
            ],
            "timeline": "Good planning saves ₹1-2L in interest over loan lifetime"
        }
    }
    
    return tips_database.get(topic, {
        "title": "💡 General Financial Tips",
        "tips": [
            "Save first, spend later",
            "Emergency fund is non-negotiable",
            "Invest regularly through SIP",
            "Avoid lifestyle inflation",
            "Learn about money - it's not taught in school!"
        ]
    })
