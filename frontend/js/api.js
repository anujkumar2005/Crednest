/**
 * CredNest AI - API Helper
 * Centralized API calls
 */

const CredNestAPI = {
    // Authentication
    auth: {
        async login(email, password) {
            return await API.post('/api/auth/login', { email, password });
        },

        async register(name, email, password) {
            return await API.post('/api/auth/register', { name, email, password });
        },

        async logout() {
            return await API.post('/api/auth/logout');
        },

        async getProfile() {
            return await API.get('/api/auth/profile');
        }
    },

    // Budgeting
    budgeting: {
        async getSummary(month) {
            return await API.get(`/api/budgeting/summary?month=${month}`);
        },

        async addExpense(data) {
            return await API.post('/api/budgeting/add-expense', data);
        }
    },

    // Savings
    savings: {
        async getGoals() {
            return await API.get('/api/savings/goals');
        },

        async createGoal(data) {
            return await API.post('/api/savings/create-goal', data);
        },

        async getTopBanks() {
            return await API.get('/api/savings/banks/top10');
        }
    },

    // Investments
    investments: {
        async getTopFunds() {
            return await API.get('/api/investments/funds/top10');
        },

        async calculateReturns(data) {
            return await API.post('/api/investments/calculate', data);
        }
    },

    // Loans
    loans: {
        async getTopBanks(type) {
            return await API.get(`/api/loans/banks/top20?type=${type}`);
        },

        async calculateEMI(data) {
            return await API.post('/api/loans/calculate-emi', data);
        }
    },

    // Insurance
    insurance: {
        async getTopCompanies() {
            return await API.get('/api/insurance/companies/top10');
        }
    },

    // AI Chat
    chat: {
        async sendMessage(message, sessionId) {
            return await API.post('/api/chat/message', { message, session_id: sessionId });
        },

        async getHistory(sessionId) {
            return await API.get(`/api/chat/history/${sessionId}`);
        }
    }
};

window.CredNestAPI = CredNestAPI;
