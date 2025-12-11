"""
CredNest AI - Database Seed Data (Fixed)
Populate database with Top 20 Banks, Top 10 Insurance Companies, and Top 10 Investment Funds
Fixed to match current model schema
"""

from datetime import datetime

def seed_banks(db, Bank):
    """Seed Top 20 Indian Banks with realistic data"""
    banks_data = [
        {
            'name': 'State Bank of India',
            'logo_url': 'https://via.placeholder.com/100x100/1f4788/ffffff?text=SBI',
            'personal_loan_rate': 10.30,
            'home_loan_rate': 8.50,
            'car_loan_rate': 8.75,
            'education_loan_rate': 9.05,
            'processing_fee': 1.5,
            'min_loan_amount': 50000,
            'max_loan_amount': 50000000,
            'max_tenure_years': 20,
            'rating': 4.5,
            'customer_care': '1800 11 2211',
            'website': 'https://www.sbi.co.in',
            'description': 'India\'s largest public sector bank with extensive network and competitive rates.'
        },
        {
            'name': 'HDFC Bank',
            'logo_url': 'https://via.placeholder.com/100x100/004c8f/ffffff?text=HDFC',
            'personal_loan_rate': 10.50,
            'home_loan_rate': 8.40,
            'car_loan_rate': 8.50,
            'education_loan_rate': 9.50,
            'processing_fee': 2.0,
            'min_loan_amount': 50000,
            'max_loan_amount': 75000000,
            'max_tenure_years': 25,
            'rating': 4.7,
            'customer_care': '1800 202 6161',
            'website': 'https://www.hdfcbank.com',
            'description': 'Leading private sector bank known for excellent customer service and digital banking.'
        },
        {
            'name': 'ICICI Bank',
            'logo_url': 'https://via.placeholder.com/100x100/f37021/ffffff?text=ICICI',
            'personal_loan_rate': 10.75,
            'home_loan_rate': 8.40,
            'car_loan_rate': 8.70,
            'education_loan_rate': 9.50,
            'processing_fee': 2.0,
            'min_loan_amount': 50000,
            'max_loan_amount': 50000000,
            'max_tenure_years': 20,
            'rating': 4.6,
            'customer_care': '1800 200 3344',
            'website': 'https://www.icicibank.com',
            'description': 'Second largest private sector bank with innovative digital solutions.'
        },
        {
            'name': 'Axis Bank',
            'logo_url': 'https://via.placeholder.com/100x100/800020/ffffff?text=AXIS',
            'personal_loan_rate': 10.49,
            'home_loan_rate': 8.75,
            'car_loan_rate': 8.80,
            'education_loan_rate': 13.70,
            'processing_fee': 2.0,
            'min_loan_amount': 50000,
            'max_loan_amount': 50000000,
            'max_tenure_years': 20,
            'rating': 4.5,
            'customer_care': '1800 419 5959',
            'website': 'https://www.axisbank.com',
            'description': 'Third largest private sector bank with strong retail banking presence.'
        },
        {
            'name': 'Kotak Mahindra Bank',
            'logo_url': 'https://via.placeholder.com/100x100/ed1c24/ffffff?text=KOTAK',
            'personal_loan_rate': 10.99,
            'home_loan_rate': 8.70,
            'car_loan_rate': 8.70,
            'education_loan_rate': 16.00,
            'processing_fee': 2.5,
            'min_loan_amount': 50000,
            'max_loan_amount': 25000000,
            'max_tenure_years': 15,
            'rating': 4.6,
            'customer_care': '1800 274 0110',
            'website': 'https://www.kotak.com',
            'description': 'Premium private bank offering personalized banking solutions.'
        },
        {
            'name': 'Punjab National Bank',
            'logo_url': 'https://via.placeholder.com/100x100/0066b2/ffffff?text=PNB',
            'personal_loan_rate': 10.40,
            'home_loan_rate': 8.40,
            'car_loan_rate': 8.85,
            'education_loan_rate': 9.05,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 20000000,
            'max_tenure_years': 15,
            'rating': 4.2,
            'customer_care': '1800 180 2222',
            'website': 'https://www.pnbindia.in',
            'description': 'Second largest public sector bank with pan-India presence.'
        },
        {
            'name': 'Bank of Baroda',
            'logo_url': 'https://via.placeholder.com/100x100/ff6600/ffffff?text=BOB',
            'personal_loan_rate': 10.85,
            'home_loan_rate': 8.40,
            'car_loan_rate': 8.80,
            'education_loan_rate': 9.15,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 20000000,
            'max_tenure_years': 15,
            'rating': 4.3,
            'customer_care': '1800 258 4455',
            'website': 'https://www.bankofbaroda.in',
            'description': 'Major public sector bank with international presence.'
        },
        {
            'name': 'IDFC FIRST Bank',
            'logo_url': 'https://via.placeholder.com/100x100/d71920/ffffff?text=IDFC',
            'personal_loan_rate': 10.49,
            'home_loan_rate': 8.75,
            'car_loan_rate': 9.00,
            'education_loan_rate': 10.50,
            'processing_fee': 2.0,
            'min_loan_amount': 50000,
            'max_loan_amount': 10000000,
            'max_tenure_years': 10,
            'rating': 4.4,
            'customer_care': '1800 10 888',
            'website': 'https://www.idfcfirstbank.com',
            'description': 'New-age bank with industry-leading savings account interest rates.'
        },
        {
            'name': 'IndusInd Bank',
            'logo_url': 'https://via.placeholder.com/100x100/00539f/ffffff?text=INDUS',
            'personal_loan_rate': 10.49,
            'home_loan_rate': 8.75,
            'car_loan_rate': 8.75,
            'education_loan_rate': 11.75,
            'processing_fee': 2.0,
            'min_loan_amount': 50000,
            'max_loan_amount': 25000000,
            'max_tenure_years': 15,
            'rating': 4.5,
            'customer_care': '1860 500 5004',
            'website': 'https://www.indusind.com',
            'description': 'Premium private bank with focus on affluent customers.'
        },
        {
            'name': 'Yes Bank',
            'logo_url': 'https://via.placeholder.com/100x100/00539f/ffffff?text=YES',
            'personal_loan_rate': 10.99,
            'home_loan_rate': 9.00,
            'car_loan_rate': 9.25,
            'education_loan_rate': 11.50,
            'processing_fee': 2.5,
            'min_loan_amount': 50000,
            'max_loan_amount': 15000000,
            'max_tenure_years': 10,
            'rating': 4.1,
            'customer_care': '1800 1200',
            'website': 'https://www.yesbank.in',
            'description': 'Private sector bank with focus on corporate and retail banking.'
        },
        {
            'name': 'Canara Bank',
            'logo_url': 'https://via.placeholder.com/100x100/ed1c24/ffffff?text=CANARA',
            'personal_loan_rate': 10.65,
            'home_loan_rate': 8.40,
            'car_loan_rate': 8.90,
            'education_loan_rate': 9.05,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 20000000,
            'max_tenure_years': 15,
            'rating': 4.3,
            'customer_care': '1800 425 0018',
            'website': 'https://www.canarabank.com',
            'description': 'Leading public sector bank with strong South India presence.'
        },
        {
            'name': 'Union Bank of India',
            'logo_url': 'https://via.placeholder.com/100x100/0066b2/ffffff?text=UNION',
            'personal_loan_rate': 10.30,
            'home_loan_rate': 8.40,
            'car_loan_rate': 8.70,
            'education_loan_rate': 9.10,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 20000000,
            'max_tenure_years': 15,
            'rating': 4.2,
            'customer_care': '1800 22 22 44',
            'website': 'https://www.unionbankofindia.co.in',
            'description': 'Merged public sector bank with extensive branch network.'
        },
        {
            'name': 'Bank of India',
            'logo_url': 'https://via.placeholder.com/100x100/ff6600/ffffff?text=BOI',
            'personal_loan_rate': 10.50,
            'home_loan_rate': 8.50,
            'car_loan_rate': 8.85,
            'education_loan_rate': 9.15,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 20000000,
            'max_tenure_years': 15,
            'rating': 4.2,
            'customer_care': '1800 103 1906',
            'website': 'https://www.bankofindia.co.in',
            'description': 'Historic public sector bank with global operations.'
        },
        {
            'name': 'Central Bank of India',
            'logo_url': 'https://via.placeholder.com/100x100/0066b2/ffffff?text=CBI',
            'personal_loan_rate': 10.75,
            'home_loan_rate': 8.50,
            'car_loan_rate': 8.95,
            'education_loan_rate': 9.20,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 15000000,
            'max_tenure_years': 15,
            'rating': 4.1,
            'customer_care': '1800 22 1911',
            'website': 'https://www.centralbankofindia.co.in',
            'description': 'Public sector bank with focus on rural and semi-urban areas.'
        },
        {
            'name': 'Indian Bank',
            'logo_url': 'https://via.placeholder.com/100x100/ed1c24/ffffff?text=IB',
            'personal_loan_rate': 10.60,
            'home_loan_rate': 8.50,
            'car_loan_rate': 8.90,
            'education_loan_rate': 9.15,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 15000000,
            'max_tenure_years': 15,
            'rating': 4.2,
            'customer_care': '1800 425 00 000',
            'website': 'https://www.indianbank.in',
            'description': 'Public sector bank with strong presence in Tamil Nadu.'
        },
        {
            'name': 'Indian Overseas Bank',
            'logo_url': 'https://via.placeholder.com/100x100/0066b2/ffffff?text=IOB',
            'personal_loan_rate': 10.70,
            'home_loan_rate': 8.55,
            'car_loan_rate': 8.95,
            'education_loan_rate': 9.20,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 15000000,
            'max_tenure_years': 15,
            'rating': 4.1,
            'customer_care': '1800 425 4445',
            'website': 'https://www.iob.in',
            'description': 'Public sector bank with international operations.'
        },
        {
            'name': 'UCO Bank',
            'logo_url': 'https://via.placeholder.com/100x100/ff6600/ffffff?text=UCO',
            'personal_loan_rate': 10.65,
            'home_loan_rate': 8.50,
            'car_loan_rate': 8.90,
            'education_loan_rate': 9.15,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 15000000,
            'max_tenure_years': 15,
            'rating': 4.1,
            'customer_care': '1800 103 0123',
            'website': 'https://www.ucobank.com',
            'description': 'Public sector bank with focus on Eastern India.'
        },
        {
            'name': 'Punjab & Sind Bank',
            'logo_url': 'https://via.placeholder.com/100x100/0066b2/ffffff?text=PSB',
            'personal_loan_rate': 10.80,
            'home_loan_rate': 8.55,
            'car_loan_rate': 9.00,
            'education_loan_rate': 9.25,
            'processing_fee': 1.0,
            'min_loan_amount': 25000,
            'max_loan_amount': 10000000,
            'max_tenure_years': 15,
            'rating': 4.0,
            'customer_care': '1800 419 8300',
            'website': 'https://www.psbindia.com',
            'description': 'Public sector bank serving Northern India.'
        },
        {
            'name': 'Bandhan Bank',
            'logo_url': 'https://via.placeholder.com/100x100/ed1c24/ffffff?text=BANDHAN',
            'personal_loan_rate': 11.25,
            'home_loan_rate': 9.00,
            'car_loan_rate': 9.25,
            'education_loan_rate': 11.00,
            'processing_fee': 2.0,
            'min_loan_amount': 50000,
            'max_loan_amount': 10000000,
            'max_tenure_years': 10,
            'rating': 4.3,
            'customer_care': '1800 258 8181',
            'website': 'https://www.bandhanbank.com',
            'description': 'Microfinance-turned-bank with focus on inclusive banking.'
        },
        {
            'name': 'Federal Bank',
            'logo_url': 'https://via.placeholder.com/100x100/0066b2/ffffff?text=FEDERAL',
            'personal_loan_rate': 10.75,
            'home_loan_rate': 8.80,
            'car_loan_rate': 9.00,
            'education_loan_rate': 10.50,
            'processing_fee': 2.0,
            'min_loan_amount': 50000,
            'max_loan_amount': 15000000,
            'max_tenure_years': 15,
            'rating': 4.4,
            'customer_care': '1800 420 1199',
            'website': 'https://www.federalbank.co.in',
            'description': 'Private sector bank with strong Kerala presence.'
        }
    ]
    
    for bank_data in banks_data:
        bank = Bank(**bank_data)
        db.session.add(bank)
    
    print(f"✓ Seeded {len(banks_data)} banks")


def seed_insurance_companies(db, InsuranceCompany):
    """Seed Top 10 Insurance Companies with realistic data"""
    # Insurance model needs to be checked - using basic fields
    insurance_data = [
        {
            'name': 'LIC (Life Insurance Corporation)',
            'logo_url': 'https://via.placeholder.com/100x100/ed1c24/ffffff?text=LIC',
            'claim_settlement_ratio': 98.33,
            'life_insurance_premium': 500,
            'health_insurance_premium': 5000,
            'vehicle_insurance_premium': 2500,
            'coverage_amount': 10000000,
            'rating': 4.6,
            'customer_care': '022-68276827',
            'website': 'https://www.licindia.in',
            'description': 'India\'s largest and most trusted life insurance provider with 98%+ claim settlement ratio.'
        },
        {
            'name': 'HDFC Life',
            'logo_url': 'https://via.placeholder.com/100x100/004c8f/ffffff?text=HDFC+LIFE',
            'claim_settlement_ratio': 98.01,
            'life_insurance_premium': 600,
            'health_insurance_premium': 6000,
            'vehicle_insurance_premium': 3000,
            'coverage_amount': 5000000,
            'rating': 4.7,
            'customer_care': '1860 267 9999',
            'website': 'https://www.hdfclife.com',
            'description': 'Leading private life insurer with innovative products and excellent service.'
        },
        {
            'name': 'SBI Life',
            'logo_url': 'https://via.placeholder.com/100x100/1f4788/ffffff?text=SBI+LIFE',
            'claim_settlement_ratio': 97.79,
            'life_insurance_premium': 550,
            'health_insurance_premium': 5500,
            'vehicle_insurance_premium': 2800,
            'coverage_amount': 7500000,
            'rating': 4.6,
            'customer_care': '1800 267 9090',
            'website': 'https://www.sbilife.co.in',
            'description': 'Trusted life insurance from SBI group with comprehensive coverage options.'
        },
        {
            'name': 'ICICI Prudential',
            'logo_url': 'https://via.placeholder.com/100x100/f37021/ffffff?text=ICICI+PRU',
            'claim_settlement_ratio': 98.58,
            'life_insurance_premium': 650,
            'health_insurance_premium': 6500,
            'vehicle_insurance_premium': 3200,
            'coverage_amount': 6000000,
            'rating': 4.7,
            'customer_care': '1860 266 7766',
            'website': 'https://www.iciciprulife.com',
            'description': 'Premium life insurance with high claim settlement ratio and digital convenience.'
        },
        {
            'name': 'Max Life Insurance',
            'logo_url': 'https://via.placeholder.com/100x100/ed1c24/ffffff?text=MAX+LIFE',
            'claim_settlement_ratio': 99.51,
            'life_insurance_premium': 700,
            'health_insurance_premium': 7000,
            'vehicle_insurance_premium': 3500,
            'coverage_amount': 5000000,
            'rating': 4.8,
            'customer_care': '1860 120 5577',
            'website': 'https://www.maxlifeinsurance.com',
            'description': 'Industry-leading claim settlement ratio with customer-first approach.'
        },
        {
            'name': 'Bajaj Allianz Life',
            'logo_url': 'https://via.placeholder.com/100x100/0066b2/ffffff?text=BAJAJ',
            'claim_settlement_ratio': 97.37,
            'life_insurance_premium': 600,
            'health_insurance_premium': 6000,
            'vehicle_insurance_premium': 3000,
            'coverage_amount': 4000000,
            'rating': 4.5,
            'customer_care': '1800 209 7272',
            'website': 'https://www.bajajallianzlife.com',
            'description': 'Comprehensive life insurance solutions with flexible premium options.'
        },
        {
            'name': 'Tata AIA Life',
            'logo_url': 'https://via.placeholder.com/100x100/1f4788/ffffff?text=TATA+AIA',
            'claim_settlement_ratio': 98.03,
            'life_insurance_premium': 650,
            'health_insurance_premium': 6500,
            'vehicle_insurance_premium': 3200,
            'coverage_amount': 4500000,
            'rating': 4.6,
            'customer_care': '1860 266 9966',
            'website': 'https://www.tataaia.com',
            'description': 'Trusted Tata brand with global AIA expertise in life insurance.'
        },
        {
            'name': 'Aditya Birla Sun Life',
            'logo_url': 'https://via.placeholder.com/100x100/ff6600/ffffff?text=ABSLI',
            'claim_settlement_ratio': 97.26,
            'life_insurance_premium': 600,
            'health_insurance_premium': 6000,
            'vehicle_insurance_premium': 3000,
            'coverage_amount': 4000000,
            'rating': 4.5,
            'customer_care': '1800 270 7000',
            'website': 'https://lifeinsurance.adityabirlacapital.com',
            'description': 'Part of Aditya Birla Group offering diverse life insurance products.'
        },
        {
            'name': 'Kotak Life Insurance',
            'logo_url': 'https://via.placeholder.com/100x100/ed1c24/ffffff?text=KOTAK',
            'claim_settlement_ratio': 98.75,
            'life_insurance_premium': 650,
            'health_insurance_premium': 6500,
            'vehicle_insurance_premium': 3200,
            'coverage_amount': 5000000,
            'rating': 4.7,
            'customer_care': '1800 209 8800',
            'website': 'https://www.kotaklife.com',
            'description': 'Premium life insurance with high claim settlement and personalized service.'
        },
        {
            'name': 'Star Health Insurance',
            'logo_url': 'https://via.placeholder.com/100x100/ed1c24/ffffff?text=STAR',
            'claim_settlement_ratio': 89.34,
            'life_insurance_premium': 500,
            'health_insurance_premium': 4500,
            'vehicle_insurance_premium': 2500,
            'coverage_amount': 5000000,
            'rating': 4.4,
            'customer_care': '1800 425 2255',
            'website': 'https://www.starhealth.in',
            'description': 'India\'s first standalone health insurance company with largest hospital network.'
        }
    ]
    
    for insurance in insurance_data:
        company = InsuranceCompany(**insurance)
        db.session.add(company)
    
    print(f"✓ Seeded {len(insurance_data)} insurance companies")


def seed_investment_funds(db, InvestmentFund):
    """Seed Top 10 Investment Funds with realistic data"""
    funds_data = [
        {
            'fund_name': 'SBI Bluechip Fund',
            'fund_type': 'Large Cap Equity',
            'amc_name': 'SBI Mutual Fund',
            'nav': 72.45,
            'returns_1yr': 18.5,
            'returns_3yr': 22.3,
            'returns_5yr': 19.8,
            'expense_ratio': 0.68,
            'min_investment': 5000,
            'min_sip': 500,
            'risk_level': 'Moderate',
            'rating': 4.5,
            'description': 'Invests in large-cap stocks with consistent long-term returns.'
        },
        {
            'fund_name': 'HDFC Top 100 Fund',
            'fund_type': 'Large Cap Equity',
            'amc_name': 'HDFC Mutual Fund',
            'nav': 845.32,
            'returns_1yr': 19.2,
            'returns_3yr': 23.1,
            'returns_5yr': 20.5,
            'expense_ratio': 0.85,
            'min_investment': 5000,
            'min_sip': 500,
            'risk_level': 'Moderate',
            'rating': 4.7,
            'description': 'Flagship large-cap fund with proven track record.'
        },
        {
            'fund_name': 'ICICI Prudential Bluechip Fund',
            'fund_type': 'Large Cap Equity',
            'amc_name': 'ICICI Prudential MF',
            'nav': 98.76,
            'returns_1yr': 17.8,
            'returns_3yr': 21.5,
            'returns_5yr': 19.2,
            'expense_ratio': 0.92,
            'min_investment': 5000,
            'min_sip': 100,
            'risk_level': 'Moderate',
            'rating': 4.6,
            'description': 'Diversified large-cap portfolio with quality stocks.'
        },
        {
            'fund_name': 'Axis Midcap Fund',
            'fund_type': 'Mid Cap Equity',
            'amc_name': 'Axis Mutual Fund',
            'nav': 95.23,
            'returns_1yr': 25.4,
            'returns_3yr': 28.7,
            'returns_5yr': 24.3,
            'expense_ratio': 0.75,
            'min_investment': 5000,
            'min_sip': 500,
            'risk_level': 'High',
            'rating': 4.8,
            'description': 'Top-performing mid-cap fund with excellent stock selection.'
        },
        {
            'fund_name': 'Kotak Emerging Equity Fund',
            'fund_type': 'Mid Cap Equity',
            'amc_name': 'Kotak Mahindra MF',
            'nav': 78.54,
            'returns_1yr': 24.1,
            'returns_3yr': 27.3,
            'returns_5yr': 23.5,
            'expense_ratio': 0.88,
            'min_investment': 5000,
            'min_sip': 1000,
            'risk_level': 'High',
            'rating': 4.7,
            'description': 'Focuses on emerging mid-cap companies with growth potential.'
        },
        {
            'fund_name': 'Parag Parikh Flexi Cap Fund',
            'fund_type': 'Flexi Cap Equity',
            'amc_name': 'PPFAS Mutual Fund',
            'nav': 68.92,
            'returns_1yr': 21.3,
            'returns_3yr': 25.8,
            'returns_5yr': 22.1,
            'expense_ratio': 0.68,
            'min_investment': 1000,
            'min_sip': 1000,
            'risk_level': 'Moderate',
            'rating': 4.9,
            'description': 'Unique flexi-cap fund with global equity exposure.'
        },
        {
            'fund_name': 'Mirae Asset Large Cap Fund',
            'fund_type': 'Large Cap Equity',
            'amc_name': 'Mirae Asset MF',
            'nav': 92.15,
            'returns_1yr': 20.5,
            'returns_3yr': 24.2,
            'returns_5yr': 21.3,
            'expense_ratio': 0.52,
            'min_investment': 5000,
            'min_sip': 1000,
            'risk_level': 'Moderate',
            'rating': 4.7,
            'description': 'Low-cost large-cap fund with consistent performance.'
        },
        {
            'fund_name': 'SBI Small Cap Fund',
            'fund_type': 'Small Cap Equity',
            'amc_name': 'SBI Mutual Fund',
            'nav': 125.67,
            'returns_1yr': 28.9,
            'returns_3yr': 32.4,
            'returns_5yr': 26.8,
            'expense_ratio': 0.85,
            'min_investment': 5000,
            'min_sip': 500,
            'risk_level': 'Very High',
            'rating': 4.6,
            'description': 'High-growth small-cap fund for aggressive investors.'
        },
        {
            'fund_name': 'HDFC Hybrid Equity Fund',
            'fund_type': 'Hybrid - Aggressive',
            'amc_name': 'HDFC Mutual Fund',
            'nav': 115.43,
            'returns_1yr': 16.2,
            'returns_3yr': 19.5,
            'returns_5yr': 17.8,
            'expense_ratio': 0.95,
            'min_investment': 5000,
            'min_sip': 500,
            'risk_level': 'Moderate',
            'rating': 4.5,
            'description': 'Balanced fund with equity and debt allocation for stability.'
        },
        {
            'fund_name': 'UTI Nifty Index Fund',
            'fund_type': 'Index Fund',
            'amc_name': 'UTI Mutual Fund',
            'nav': 158.92,
            'returns_1yr': 17.5,
            'returns_3yr': 20.8,
            'returns_5yr': 18.9,
            'expense_ratio': 0.20,
            'min_investment': 5000,
            'min_sip': 500,
            'risk_level': 'Moderate',
            'rating': 4.4,
            'description': 'Low-cost index fund tracking Nifty 50 for passive investors.'
        }
    ]
    
    for fund_data in funds_data:
        fund = InvestmentFund(**fund_data)
        db.session.add(fund)
    
    print(f"✓ Seeded {len(funds_data)} investment funds")


def seed_all_data(db, Bank, InsuranceCompany, InvestmentFund):
    """Seed all data into database"""
    print("\n" + "="*70)
    print("🌱  Seeding CredNest AI Database")
    print("="*70)
    
    try:
        seed_banks(db, Bank)
        seed_insurance_companies(db, InsuranceCompany)
        seed_investment_funds(db, InvestmentFund)
        
        db.session.commit()
        
        print("="*70)
        print("✅  Database seeding completed successfully!")
        print("="*70)
        print(f"📊  Total Records:")
        print(f"   → Banks: {Bank.query.count()}")
        print(f"   → Insurance Companies: {InsuranceCompany.query.count()}")
        print(f"   → Investment Funds: {InvestmentFund.query.count()}")
        print("="*70 + "\n")
        
        return True
        
    except Exception as e:
        db.session.rollback()
        print(f"\n❌  Error seeding database: {e}\n")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    print("This script should be run from app.py or db_init.py")
