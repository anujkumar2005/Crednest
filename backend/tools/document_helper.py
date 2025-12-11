"""
Document Requirements Helper Tool
"""

def get_document_checklist(loan_type: str, employment_type: str) -> dict:
    """
    Get required documents for loan application
    
    Args:
        loan_type: personal, home, car, business, education
        employment_type: salaried, self_employed, business
    
    Returns:
        Complete document checklist
    """
    
    # Common documents for all
    common_docs = [
        {"name": "PAN Card", "required": True, "why": "Mandatory for all financial transactions"},
        {"name": "Aadhaar Card", "required": True, "why": "Identity and address proof (e-KYC enabled)"},
        {"name": "Passport size photos", "required": True, "qty": "2 recent color photos"},
        {"name": "Bank statements", "required": True, "period": "Last 6 months", "why": "Shows income and spending patterns"},
        {"name": "Address proof", "required": True, "options": ["Aadhaar", "Passport", "Utility bill (electricity/water)", "Rent agreement"]}
    ]
    
    # Employment-specific documents
    employment_docs = {
        "salaried": [
            {"name": "Salary slips", "required": True, "period": "Last 3 months", "why": "Proof of current income"},
            {"name": "Form 16", "required": True, "period": "Last 2 years", "why": "Annual income proof with tax deduction"},
            {"name": "Employment certificate", "required": True, "why": "Confirms job and designation"},
            {"name": "Employee ID card", "required": False, "why": "Additional employment proof"},
            {"name": "Appointment letter", "required": False, "why": "Shows job start date and salary"}
        ],
        "self_employed": [
            {"name": "ITR (Income Tax Returns)", "required": True, "period": "Last 2-3 years", "why": "Primary income proof"},
            {"name": "Computation of income", "required": True, "why": "Detailed income calculation"},
            {"name": "Business registration certificate", "required": True, "why": "Proves business legitimacy"},
            {"name": "GST returns", "required": True, "period": "Last 12 months", "condition": "If GST registered"},
            {"name": "Audited financial statements", "required": True, "period": "Last 2 years", "why": "Balance sheet and P&L statement"},
            {"name": "Business bank statements", "required": True, "period": "Last 12 months"}
        ],
        "business": [
            {"name": "Business PAN", "required": True},
            {"name": "GST Registration certificate", "required": True, "condition": "If applicable"},
            {"name": "Partnership deed / MOA & AOA", "required": True, "why": "Business structure proof"},
            {"name": "ITR of business", "required": True, "period": "Last 3 years"},
            {"name": "Audited financials", "required": True, "period": "Last 2 years"},
            {"name": "Business continuity proof", "required": True, "examples": ["Shop license", "Office lease", "Client contracts"]},
            {"name": "Current liabilities statement", "required": True, "why": "Shows existing business loans"}
        ]
    }
    
    # Loan-specific additional documents
    loan_specific_docs = {
        "personal": [],  # No additional docs needed
        
        "home": [
            {"name": "Property documents", "required": True, "details": [
                "Sale agreement / Allotment letter",
                "Approved building plan",
                "NOC from builder/society",
                "Chain of ownership documents",
                "Property tax receipts (last 3 years)",
                "Possession certificate",
                "Encumbrance certificate (EC) for last 13-30 years",
                "Mother deed / Previous sale deeds"
            ]},
            {"name": "Property valuation report", "required": True, "by": "Bank-approved valuer"},
            {"name": "Builder registration", "required": True, "condition": "For under-construction property", "details": ["RERA registration", "Construction completion certificate"]}
        ],
        
        "car": [
            {"name": "Vehicle quotation", "required": True, "from": "Dealer", "should_include": ["On-road price", "Insurance", "Registration"]},
            {"name": "Proforma invoice", "required": True},
            {"name": "Vehicle insurance", "required": True, "type": "Comprehensive (required by lender)"},
            {"name": "RC (Registration Certificate)", "required": True, "condition": "For used car"},
            {"name": "RC transfer documents", "required": True, "condition": "For used car"},
            {"name": "Previous loan closure certificate", "required": True, "condition": "If used car had loan"}
        ],
        
        "education": [
            {"name": "Admission letter", "required": True, "from": "Educational institution"},
            {"name": "Fee structure", "required": True, "should_show": ["Tuition fees", "Hostel", "Other expenses"]},
            {"name": "Mark sheets", "required": True, "which": ["10th", "12th", "Graduation (if applicable)"]},
            {"name": "Entrance exam scorecard", "required": True, "examples": ["CAT", "GMAT", "GRE", "JEE", "NEET"]},
            {"name": "Co-applicant income proof", "required": True, "why": "Parent/guardian financials"},
            {"name": "Passport", "required": True, "condition": "For foreign education"},
            {"name": "Visa documents", "required": True, "condition": "For foreign education"},
            {"name": "Scholarship letter", "required": False, "benefit": "Reduces loan amount"}
        ],
        
        "business": [
            {"name": "Detailed business plan", "required": True, "should_include": [
                "Business model and revenue streams",
                "Market analysis and competition",
                "Financial projections (3-5 years)",
                "Use of loan funds (detailed breakdown)",
                "Risk analysis and mitigation"
            ]},
            {"name": "Existing loan statements", "required": True, "why": "All business and personal loans"},
            {"name": "Collateral documents", "required": True, "condition": "For secured business loans", "options": [
                "Property papers",
                "Fixed deposits",
                "Machinery invoices",
                "Inventory valuation"
            ]},
            {"name": "Client contracts / Purchase orders", "required": False, "benefit": "Shows business viability"},
            {"name": "CIBIL report", "required": True, "for": "Business and all directors/partners"}
        ]
    }
    
    # Build complete checklist
    employment_category = employment_docs.get(employment_type, employment_docs["salaried"])
    loan_category = loan_specific_docs.get(loan_type, [])
    
    return {
        "loan_type": loan_type,
        "employment_type": employment_type,
        "summary": {
            "total_documents": len(common_docs) + len(employment_category) + len(loan_category),
            "mandatory": len([d for d in (common_docs + employment_category + loan_category) if d.get("required")]),
            "optional": len([d for d in (common_docs + employment_category + loan_category) if not d.get("required")])
        },
        "common_documents": common_docs,
        "employment_documents": employment_category,
        "loan_specific_documents": loan_category,
        "pro_tips": [
            "✓ Self-attest all photocopies - saves time at bank",
            "✓ Carry original documents for verification",
            "✓ Keep 3-4 sets of all documents ready",
            "✓ Digital copies (PDF) handy for online applications",
            "✓ Ensure all documents have same name as per PAN",
            "✓ Current address should match across all documents",
            "✓ Get missing documents BEFORE applying - incomplete applications get rejected"
        ],
        "common_mistakes": [
            "✗ Mismatched signatures across documents",
            "✗ Old photos or wrong size",
            "✗ Bank statements without bank stamp",
            "✗ Unsigned Form 16 or ITR",
            "✗ Property documents not in applicant's name",
            "✗ Expired address proofs"
        ]
    }
