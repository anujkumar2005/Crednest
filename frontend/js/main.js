/**
 * CredNest AI - Main JavaScript
 * Core functionality and utilities
 */

// ============================================================================
// GLOBAL CONFIGURATION
// ============================================================================

const CREDNEST = {
    API_BASE: window.location.origin,
    VERSION: '1.0.0',
    DEBUG: true
};

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

/**
 * Show notification
 */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.innerHTML = `
        <div class="alert-icon">
            ${type === 'success' ? '✓' : type === 'error' ? '✗' : 'ℹ'}
        </div>
        <div class="alert-content">${message}</div>
    `;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/**
 * Format currency
 */
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 0
    }).format(amount);
}

/**
 * Format date
 */
function formatDate(date) {
    return new Intl.DateTimeFormat('en-IN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(new Date(date));
}

/**
 * Debounce function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Throttle function
 */
function throttle(func, limit) {
    let inThrottle;
    return function (...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// ============================================================================
// API HELPER
// ============================================================================

class API {
    static async request(endpoint, options = {}) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        };

        try {
            const response = await fetch(`${CREDNEST.API_BASE}${endpoint}`, config);
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Request failed');
            }

            return data;
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    static get(endpoint) {
        return this.request(endpoint);
    }

    static post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    static put(endpoint, data) {
        return this.request(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    static delete(endpoint) {
        return this.request(endpoint, {
            method: 'DELETE'
        });
    }
}

// ============================================================================
// MODAL MANAGER
// ============================================================================

class Modal {
    constructor(id) {
        this.modal = document.getElementById(id);
        this.overlay = this.modal?.querySelector('.modal-overlay');

        if (this.modal) {
            this.setupEvents();
        }
    }

    setupEvents() {
        const closeBtn = this.modal.querySelector('.modal-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => this.close());
        }

        this.overlay?.addEventListener('click', (e) => {
            if (e.target === this.overlay) {
                this.close();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.modal.classList.contains('active')) {
                this.close();
            }
        });
    }

    open() {
        this.modal?.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    close() {
        this.modal?.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// ============================================================================
// FORM VALIDATOR
// ============================================================================

class FormValidator {
    constructor(formId) {
        this.form = document.getElementById(formId);
        this.errors = {};
    }

    validate(rules) {
        this.errors = {};
        let isValid = true;

        for (const [field, rule] of Object.entries(rules)) {
            const input = this.form.querySelector(`[name="${field}"]`);
            const value = input?.value.trim();

            if (rule.required && !value) {
                this.errors[field] = `${rule.label} is required`;
                isValid = false;
                continue;
            }

            if (rule.minLength && value.length < rule.minLength) {
                this.errors[field] = `${rule.label} must be at least ${rule.minLength} characters`;
                isValid = false;
                continue;
            }

            if (rule.pattern && !rule.pattern.test(value)) {
                this.errors[field] = rule.message || `${rule.label} is invalid`;
                isValid = false;
                continue;
            }

            if (rule.custom && !rule.custom(value)) {
                this.errors[field] = rule.message || `${rule.label} is invalid`;
                isValid = false;
            }
        }

        this.displayErrors();
        return isValid;
    }

    displayErrors() {
        // Clear previous errors
        this.form.querySelectorAll('.error-message').forEach(el => el.remove());
        this.form.querySelectorAll('.input-field.error').forEach(el => el.classList.remove('error'));

        // Display new errors
        for (const [field, message] of Object.entries(this.errors)) {
            const input = this.form.querySelector(`[name="${field}"]`);
            if (input) {
                input.classList.add('error');
                const errorEl = document.createElement('div');
                errorEl.className = 'error-message';
                errorEl.textContent = message;
                input.parentElement.appendChild(errorEl);
            }
        }
    }
}

// ============================================================================
// LOCAL STORAGE MANAGER
// ============================================================================

class Storage {
    static set(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (error) {
            console.error('Storage Error:', error);
            return false;
        }
    }

    static get(key) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : null;
        } catch (error) {
            console.error('Storage Error:', error);
            return null;
        }
    }

    static remove(key) {
        localStorage.removeItem(key);
    }

    static clear() {
        localStorage.clear();
    }
}

// ============================================================================
// INITIALIZE ON DOM READY
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
    // Initialize animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    });

    document.querySelectorAll('[data-animate]').forEach(el => {
        observer.observe(el);
    });

    // Initialize smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            target?.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Initialize tooltips
    document.querySelectorAll('[data-tooltip]').forEach(el => {
        el.classList.add('tooltip');
    });

    console.log('CredNest AI initialized successfully!');
});

// ============================================================================
// EXPORT FOR USE
// ============================================================================

window.CredNest = {
    API,
    Modal,
    FormValidator,
    Storage,
    showNotification,
    formatCurrency,
    formatDate,
    debounce,
    throttle
};
