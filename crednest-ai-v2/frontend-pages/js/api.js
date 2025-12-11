// CredNest AI v2.0 - API Client

const API_URL = 'http://localhost:5000/api';

class APIClient {
    constructor() {
        this.token = localStorage.getItem('authToken');
    }

    setToken(token) {
        this.token = token;
        localStorage.setItem('authToken', token);
    }

    clearToken() {
        this.token = null;
        localStorage.removeItem('authToken');
    }

    getHeaders() {
        const headers = {
            'Content-Type': 'application/json'
        };

        if (this.token) {
            headers['Authorization'] = `Bearer ${this.token}`;
        }

        return headers;
    }

    async request(endpoint, options = {}) {
        try {
            const response = await fetch(`${API_URL}${endpoint}`, {
                ...options,
                headers: this.getHeaders()
            });

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    // Auth endpoints
    async register(name, email, password) {
        return this.request('/auth/register', {
            method: 'POST',
            body: JSON.stringify({ name, email, password })
        });
    }

    async login(email, password) {
        return this.request('/auth/login', {
            method: 'POST',
            body: JSON.stringify({ email, password })
        });
    }

    async getProfile() {
        return this.request('/auth/profile');
    }

    async updateProfile(data) {
        return this.request('/auth/profile', {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    // Chat endpoints
    async sendMessage(message, sessionId = null) {
        return this.request('/chat/message', {
            method: 'POST',
            body: JSON.stringify({ message, sessionId })
        });
    }

    async getChatSessions() {
        return this.request('/chat/sessions');
    }

    async getChatHistory(sessionId) {
        return this.request(`/chat/history/${sessionId}`);
    }

    async deleteSession(sessionId) {
        return this.request(`/chat/session/${sessionId}`, {
            method: 'DELETE'
        });
    }

    // Budget endpoints
    async createBudget(data) {
        return this.request('/budgets', {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async getBudgets(period = null) {
        const query = period ? `?period=${period}` : '';
        return this.request(`/budgets${query}`);
    }

    async updateBudget(id, data) {
        return this.request(`/budgets/${id}`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    async deleteBudget(id) {
        return this.request(`/budgets/${id}`, {
            method: 'DELETE'
        });
    }

    async getBudgetSummary(period = 'monthly') {
        return this.request(`/budgets/summary?period=${period}`);
    }

    // Expense endpoints
    async addExpense(data) {
        return this.request('/expenses', {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async getExpenses(filters = {}) {
        const query = new URLSearchParams(filters).toString();
        return this.request(`/expenses?${query}`);
    }

    async deleteExpense(id) {
        return this.request(`/expenses/${id}`, {
            method: 'DELETE'
        });
    }

    // Financial endpoints
    async getBanks(loanType = null, limit = 20) {
        const query = new URLSearchParams({ limit });
        if (loanType) query.append('loanType', loanType);
        return this.request(`/financial/banks?${query}`);
    }

    async getBankById(id) {
        return this.request(`/financial/banks/${id}`);
    }

    async calculateEMI(principal, rate, tenure) {
        return this.request('/financial/calculate-emi', {
            method: 'POST',
            body: JSON.stringify({ principal, rate, tenure })
        });
    }

    async checkLoanEligibility(monthlyIncome, loanAmount, cibilScore = 750) {
        return this.request('/financial/check-eligibility', {
            method: 'POST',
            body: JSON.stringify({ monthlyIncome, loanAmount, cibilScore })
        });
    }
}

// Create global instance
const api = new APIClient();

// Auth utilities
function checkAuth() {
    if (!api.token) {
        window.location.href = 'index.html';
        return false;
    }
    return true;
}

async function loadUserInfo() {
    try {
        const data = await api.getProfile();
        if (data.success) {
            return data.user;
        } else {
            api.clearToken();
            window.location.href = 'index.html';
        }
    } catch (error) {
        api.clearToken();
        window.location.href = 'index.html';
    }
}

function logout() {
    api.clearToken();
    window.location.href = 'index.html';
}

// UI utilities
function showAlert(message, type = 'success') {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    alert.style.position = 'fixed';
    alert.style.top = '20px';
    alert.style.right = '20px';
    alert.style.zIndex = '9999';
    alert.style.minWidth = '300px';
    alert.style.animation = 'slideIn 0.3s ease';

    document.body.appendChild(alert);

    setTimeout(() => {
        alert.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => alert.remove(), 300);
    }, 3000);
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        maximumFractionDigits: 0
    }).format(amount);
}

function formatDate(date) {
    return new Date(date).toLocaleDateString('en-IN', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

// Add animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideOut {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(100px);
        }
    }
`;
document.head.appendChild(style);
