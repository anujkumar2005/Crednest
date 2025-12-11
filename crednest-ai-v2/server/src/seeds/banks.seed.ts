import mongoose from 'mongoose';
import Bank from '../models/Bank';
import config from '../config/environment';

const banksData = [
    {
        name: 'State Bank of India (SBI)',
        logoUrl: 'https://www.sbi.co.in/documents/16012/1400784/SBI-Logo.jpg',
        homeLoanRate: 8.50,
        personalLoanRate: 10.30,
        carLoanRate: 8.70,
        educationLoanRate: 9.05,
        processingFee: 0.35,
        minCibilScore: 750,
        maxLoanAmount: 10000000,
        minLoanAmount: 100000,
        maxTenureYears: 30,
        description: 'India\'s largest public sector bank offering comprehensive loan solutions',
        website: 'https://www.sbi.co.in',
        customerCare: '1800-11-2211',
        rating: 4.5
    },
    {
        name: 'HDFC Bank',
        homeLoanRate: 8.60,
        personalLoanRate: 10.50,
        carLoanRate: 8.75,
        educationLoanRate: 9.50,
        processingFee: 0.50,
        minCibilScore: 750,
        maxLoanAmount: 7500000,
        minLoanAmount: 100000,
        maxTenureYears: 30,
        description: 'Leading private sector bank with quick loan approvals',
        website: 'https://www.hdfcbank.com',
        customerCare: '1800-202-6161',
        rating: 4.6
    },
    {
        name: 'ICICI Bank',
        homeLoanRate: 8.65,
        personalLoanRate: 10.75,
        carLoanRate: 8.80,
        educationLoanRate: 9.60,
        processingFee: 0.50,
        minCibilScore: 750,
        maxLoanAmount: 7500000,
        minLoanAmount: 100000,
        maxTenureYears: 30,
        description: 'Comprehensive banking solutions with digital-first approach',
        website: 'https://www.icicibank.com',
        customerCare: '1860-120-7777',
        rating: 4.5
    },
    {
        name: 'Axis Bank',
        homeLoanRate: 8.70,
        personalLoanRate: 10.49,
        carLoanRate: 8.75,
        educationLoanRate: 9.70,
        processingFee: 0.50,
        minCibilScore: 750,
        maxLoanAmount: 5000000,
        minLoanAmount: 100000,
        maxTenureYears: 30,
        description: 'Fast loan processing with competitive interest rates',
        website: 'https://www.axisbank.com',
        customerCare: '1860-419-5555',
        rating: 4.4
    },
    {
        name: 'Punjab National Bank (PNB)',
        homeLoanRate: 8.40,
        personalLoanRate: 9.95,
        carLoanRate: 8.65,
        educationLoanRate: 8.85,
        processingFee: 0.35,
        minCibilScore: 700,
        maxLoanAmount: 5000000,
        minLoanAmount: 100000,
        maxTenureYears: 30,
        description: 'Government bank with affordable loan options',
        website: 'https://www.pnbindia.in',
        customerCare: '1800-180-2222',
        rating: 4.2
    },
    {
        name: 'Bank of Baroda',
        homeLoanRate: 8.45,
        personalLoanRate: 10.15,
        carLoanRate: 8.70,
        educationLoanRate: 8.95,
        processingFee: 0.30,
        minCibilScore: 700,
        maxLoanAmount: 5000000,
        minLoanAmount: 100000,
        maxTenureYears: 30,
        description: 'Trusted public sector bank with extensive network',
        website: 'https://www.bankofbaroda.in',
        customerCare: '1800-258-4455',
        rating: 4.3
    },
    {
        name: 'Kotak Mahindra Bank',
        homeLoanRate: 8.70,
        personalLoanRate: 10.99,
        carLoanRate: 8.85,
        educationLoanRate: 9.75,
        processingFee: 0.50,
        minCibilScore: 750,
        maxLoanAmount: 5000000,
        minLoanAmount: 100000,
        maxTenureYears: 30,
        description: 'Premium banking with personalized loan solutions',
        website: 'https://www.kotak.com',
        customerCare: '1860-266-2666',
        rating: 4.5
    },
    {
        name: 'IndusInd Bank',
        homeLoanRate: 8.75,
        personalLoanRate: 10.49,
        carLoanRate: 8.90,
        educationLoanRate: 9.80,
        processingFee: 0.50,
        minCibilScore: 750,
        maxLoanAmount: 5000000,
        minLoanAmount: 100000,
        maxTenureYears: 25,
        description: 'Innovative banking with quick loan disbursals',
        website: 'https://www.indusind.com',
        customerCare: '1860-500-5004',
        rating: 4.4
    },
    {
        name: 'Yes Bank',
        homeLoanRate: 8.80,
        personalLoanRate: 10.99,
        carLoanRate: 8.95,
        educationLoanRate: 9.85,
        processingFee: 0.50,
        minCibilScore: 750,
        maxLoanAmount: 5000000,
        minLoanAmount: 100000,
        maxTenureYears: 25,
        description: 'Modern banking solutions with competitive rates',
        website: 'https://www.yesbank.in',
        customerCare: '1800-1200',
        rating: 4.2
    },
    {
        name: 'Canara Bank',
        homeLoanRate: 8.40,
        personalLoanRate: 10.05,
        carLoanRate: 8.65,
        educationLoanRate: 8.90,
        processingFee: 0.35,
        minCibilScore: 700,
        maxLoanAmount: 5000000,
        minLoanAmount: 100000,
        maxTenureYears: 30,
        description: 'Reliable public sector bank with low interest rates',
        website: 'https://www.canarabank.com',
        customerCare: '1800-425-0018',
        rating: 4.3
    }
];

export const seedBanks = async () => {
    try {
        await mongoose.connect(config.mongoUri);
        console.log('✓ Connected to MongoDB');

        // Clear existing banks
        await Bank.deleteMany({});
        console.log('✓ Cleared existing banks');

        // Insert new banks
        await Bank.insertMany(banksData);
        console.log(`✓ Seeded ${banksData.length} banks`);

        await mongoose.connection.close();
        console.log('✓ Database connection closed');

        process.exit(0);
    } catch (error) {
        console.error('✗ Seed error:', error);
        process.exit(1);
    }
};

// Run if called directly
if (require.main === module) {
    seedBanks();
}
