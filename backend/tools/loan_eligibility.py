"""
Loan Eligibility Checker Tool
"""

def check_loan_eligibility(monthly_income: float, loan_amount: float, loan_type: str, 
                          credit_score: int = None, employment_type: str = None, 
                          existing_loans: bool = False) -> dict:
    """
    Check loan eligibility based on financial parameters
    
    Args:
        monthly_income: Monthly income in INR
        loan_amount: Requested loan amount in INR
        loan_type: Type of loan (personal, home, car, business, education)
        credit_score: CIBIL score (300-900)
        employment_type: salaried, self_employed, business
        existing_loans: Whether user has existing loans
    
    Returns:
        Dictionary with eligibility status and details
    """
    
    # Calculate maximum eligible loan (50x monthly income)
    max_eligible = monthly_income * 50
    
    # Calculate EMI to income ratio (should be <50%)
    estimated_emi = loan_amount * 0.015  # Rough estimate: 1.5% of loan amount
    emi_ratio = (estimated_emi / monthly_income) * 100
    
    # Initialize results
    eligible = True
    reasons = []
    suggestions = []
    risk_level = "Low"
    
    # Check 1: Loan amount vs income
    if loan_amount > max_eligible:
        eligible = False
        reasons.append(f"Requested ₹{loan_amount:,.0f} exceeds max eligible ₹{max_eligible:,.0f}")
        suggestions.append(f"Consider reducing loan amount to ₹{max_eligible:,.0f} or below")
    
    # Check 2: Credit score
    if credit_score:
        if credit_score < 600:
            eligible = False
            risk_level = "High"
            reasons.append(f"Credit score {credit_score} is too low (minimum 600 required)")
            suggestions.append("Improve credit score before applying - pay bills on time, reduce credit utilization")
        elif credit_score < 700:
            risk_level = "Medium"
            suggestions.append("Credit score {credit_score} is acceptable but improving to 700+ will get better rates")
        else:
            suggestions.append(f"Excellent credit score {credit_score}! You qualify for best interest rates")
    
    # Check 3: EMI to income ratio
    if emi_ratio > 50:
        eligible = False
        reasons.append(f"EMI would be {emi_ratio:.1f}% of income (max allowed: 50%)")
        suggestions.append("Reduce loan amount or extend tenure to lower EMI")
    elif emi_ratio > 40:
        risk_level = "Medium"
        suggestions.append(f"EMI is {emi_ratio:.1f}% of income - manageable but leaves little room for savings")
    
    # Check 4: Existing loans
    if existing_loans:
        suggestions.append("Existing loans will be considered - ensure combined EMI stays under 50% of income")
    
    # Loan type specific advice
    loan_specific_tips = {
        "personal": ["No collateral required", "Quick approval (2-7 days)", "Use for emergencies or consolidation"],
        "home": ["Requires property as collateral", "Longer tenure (up to 30 years)", "Tax benefits under Section 80C and 24(b)"],
        "car": ["Vehicle is collateral", "Quick approval (2-5 days)", "Covers up to 90% of vehicle cost"],
        "business": ["Business plan required", "Collateral usually needed", "Use for working capital or expansion"],
        "education": ["Covers tuition + living expenses", "Moratorium period available", "Some loans have govt subsidy"]
    }
    
    # Build response
    return {
        "eligible": eligible,
        "risk_level": risk_level,
        "loan_type": loan_type,
        "requested_amount": loan_amount,
        "max_eligible_amount": max_eligible,
        "monthly_income": monthly_income,
        "credit_score": credit_score,
        "estimated_monthly_emi": round(estimated_emi, 2),
        "emi_to_income_ratio": round(emi_ratio, 1),
        "reasons": reasons if not eligible else ["✓ All basic eligibility criteria met"],
        "suggestions": suggestions,
        "loan_specific_tips": loan_specific_tips.get(loan_type, []),
        "next_steps": [
            "1. Gather required documents (PAN, Aadhaar, income proof)",
            "2. Check with 3-4 banks for best rates",
            "3. Get pre-approval to know exact loan amount",
            "4. Compare processing fees and hidden charges",
            "5. Read loan agreement carefully before signing"
        ] if eligible else [
            "1. Address the eligibility issues mentioned above",
            "2. Improve credit score if needed",
            "3. Reduce loan amount or increase income",
            "4. Consider a co-applicant for better eligibility",
            "5. Consult with a financial advisor"
        ]
    }
