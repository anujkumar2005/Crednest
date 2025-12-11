"""
EMI Calculator Tool
"""

def calculate_emi(loan_amount: float, interest_rate: float, tenure_months: int) -> dict:
    """
    Calculate EMI using standard formula
    
    Args:
        loan_amount: Principal amount in INR
        interest_rate: Annual interest rate (e.g., 10.5 for 10.5%)
        tenure_months: Loan tenure in months
    
    Returns:
        Dictionary with EMI and breakdown
    """
    
    # Monthly interest rate
    monthly_rate = interest_rate / 12 / 100
    
    # EMI Formula: P × r × (1 + r)^n / ((1 + r)^n - 1)
    if monthly_rate == 0:
        emi = loan_amount / tenure_months
    else:
        emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** tenure_months) / (
            ((1 + monthly_rate) ** tenure_months) - 1
        )
    
    total_amount = emi * tenure_months
    total_interest = total_amount - loan_amount
    
    # Year-wise breakdown
    yearly_breakdown = []
    remaining_principal = loan_amount
    
    for year in range(1, (tenure_months // 12) + 2):
        year_start_month = (year - 1) * 12 + 1
        year_end_month = min(year * 12, tenure_months)
        
        if year_start_month > tenure_months:
            break
        
        year_interest = 0
        year_principal = 0
        
        for month in range(year_start_month, year_end_month + 1):
            month_interest = remaining_principal * monthly_rate
            month_principal = emi - month_interest
            
            year_interest += month_interest
            year_principal += month_principal
            remaining_principal -= month_principal
        
        yearly_breakdown.append({
            "year": year,
            "opening_balance": round(remaining_principal + year_principal, 2),
            "principal_paid": round(year_principal, 2),
            "interest_paid": round(year_interest, 2),
            "total_paid": round(year_principal + year_interest, 2),
            "closing_balance": round(max(0, remaining_principal), 2)
        })
    
    return {
        "loan_amount": round(loan_amount, 2),
        "interest_rate": interest_rate,
        "tenure_months": tenure_months,
        "tenure_years": round(tenure_months / 12, 1),
        "monthly_emi": round(emi, 2),
        "total_amount_payable": round(total_amount, 2),
        "total_interest": round(total_interest, 2),
        "interest_percentage": round((total_interest / loan_amount) * 100, 1),
        "yearly_breakdown": yearly_breakdown,
        "tips": [
            f"Your EMI of ₹{emi:,.0f} should be <40% of your monthly income",
            "Consider part-payment to reduce interest burden",
            "Check if your bank charges pre-payment penalties",
            f"Total interest of ₹{total_interest:,.0f} is {(total_interest/loan_amount)*100:.1f}% of principal"
        ]
    }
