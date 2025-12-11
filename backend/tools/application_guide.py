"""
Loan Application Guidance Tool
"""

def get_application_guidance(loan_type: str, employment_type: str = None) -> dict:
    """
    Step-by-step loan application guidance
    
    Args:
        loan_type: Type of loan
        employment_type: Optional employment type for personalized guidance
    
    Returns:
        Complete application guide
    """
    
    # Timeline varies by loan type
    timelines = {
        "personal": {"approval": "2-7 days", "disbursement": "24-48 hours after approval", "total": "3-10 days"},
        "home": {"approval": "2-4 weeks", "disbursement": "In tranches over 6-24 months", "total": "1-3 months for sanction"},
        "car": {"approval": "2-5 days", "disbursement": "Same day as approval", "total": "3-7 days"},
        "education": {"approval": "1-2 weeks", "disbursement": "Directly to institution", "total": "2-3 weeks"},
        "business": {"approval": "2-3 weeks", "disbursement": "7-10 days after approval", "total": "3-4 weeks"}
    }
    
    # Step-by-step process
    application_steps = {
        "personal": [
            {"step": 1, "title": "Check Your Credit Score", "details": "Free on CIBIL.com - 750+ is ideal for best rates", "time": "5 minutes"},
            {"step": 2, "title": "Calculate Affordability", "details": "EMI should be <40% of monthly income. Use online calculators", "time": "10 minutes"},
            {"step": 3, "title": "Compare Banks", "details": "Check rates from SBI, HDFC, ICICI, Kotak, Axis (minimum 3 banks)", "time": "1-2 hours"},
            {"step": 4, "title": "Check Eligibility", "details": "Use bank's online eligibility calculator - saves rejection", "time": "15 minutes"},
            {"step": 5, "title": "Gather Documents", "details": "PAN, Aadhaar, salary slips (3 months), bank statements (6 months)", "time": "1-2 hours"},
            {"step": 6, "title": "Apply Online/Offline", "details": "Online is faster but branch visit may get better negotiation", "time": "30 minutes"},
            {"step": 7, "title": "Bank Verification", "details": "Bank verifies employment (HR call), residence (sometimes field visit)", "time": "2-3 days"},
            {"step": 8, "title": "Credit Appraisal", "details": "Bank checks CIBIL, repayment capacity, existing loans", "time": "2-4 days"},
            {"step": 9, "title": "Loan Approval", "details": "Sanction letter issued with final approved amount and rate", "time": "Same day"},
            {"step": 10, "title": "Agreement Signing", "details": "Read loan agreement, ECS mandate, insurance (optional but pushed)", "time": "1 hour"},
            {"step": 11, "title": "Disbursement", "details": "Amount credited to your bank account directly", "time": "24-48 hours"}
        ]
    }
    
    # Get timeline and steps
    timeline = timelines.get(loan_type, timelines["personal"])
    steps = application_steps.get(loan_type, application_steps["personal"])
    
    # Pro tips specific to loan type
    pro_tips = {
        "personal": [
            "💡 Apply to bank where you have salary account - better chances + lower rate",
            "💡 Pre-approved offers from existing bank are fastest",
            "💡 Salaried from top companies (MNCs, PSUs, Govt) get preferential rates",
            "💡 Co-applicant (spouse) improves eligibility up to 100%",
            "💡 Avoid multiple applications in one month - each hurts CIBIL score by 5-10 points"
        ],
        "home": [
            "💡 Get pre-approval BEFORE selecting property - avoids last-minute rejection",
            "💡 Bank sends valuer to assess property - ensure all paperwork is ready",
            "💡 Processing fee is 0.5-1% of loan - negotiate for waiver/reduction",
            "💡 Many banks fund only 75-80% of property value - arrange 20-25% down payment",
            "💡 Joint home loan with spouse doubles eligibility + both get tax benefits"
        ]
    }
    
    # Common mistakes to avoid
    common_mistakes = [
        "❌ Applying to 5+ banks simultaneously - looks desperate, hurts credit score",
        "❌ Hiding existing loans - bank will find out in CIBIL check",
        "❌ Providing wrong employment/income info - leads to instant rejection",
        "❌ Not reading loan agreement - hidden charges and clauses bite later",
        "❌ Taking loan insurance from bank - 2-3x more expensive than term insurance",
        "❌ Not comparing processing fees - can vary from 0% to 2%"
    ]
    
    return {
        "loan_type": loan_type,
        "employment_type": employment_type,
        "timeline": timeline,
        "steps": steps,
        "total_steps": len(steps),
        "pro_tips": pro_tips.get(loan_type, pro_tips["personal"]),
        "common_mistakes": common_mistakes,
        "quick_wins": [
            "✓ Check credit score today - free and instant",
            "✓ Use online EMI calculator to know affordable amount",
            "✓ Get salary slips and bank statements ready",
            "✓ Compare 3 banks before applying",
            "✓ Read online reviews of bank's loan process"
        ],
        "negotiation_tips": [
            "💰 Ask for processing fee waiver (works for good CIBIL scores)",
            "💰 Negotiate interest rate - 0.25-0.5% reduction possible",
            "💰 Request for waiver of prepayment charges",
            "💰 Compare and show competitor's offer - banks may match",
            "💰 Larger loan amount gives better bargaining power"
        ]
    }
