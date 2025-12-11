/**
 * CredNest AI - Chart Utilities
 * Chart.js helpers and configurations
 */

const ChartHelpers = {
    // Default chart options for dark theme
    defaultOptions: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    color: '#FFFFFF',
                    padding: 15,
                    font: { size: 12 }
                }
            },
            tooltip: {
                backgroundColor: 'rgba(18, 18, 18, 0.9)',
                titleColor: '#FFD700',
                bodyColor: '#FFFFFF',
                borderColor: 'rgba(255, 215, 0, 0.3)',
                borderWidth: 1,
                padding: 12,
                cornerRadius: 8
            }
        }
    },

    // Create doughnut chart for spending
    createSpendingChart(ctx, data) {
        return new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.values,
                    backgroundColor: [
                        '#FFD700', // Gold
                        '#00D4FF', // Blue
                        '#B794F6', // Purple
                        '#00FF88', // Green
                        '#FFB800'  // Orange
                    ],
                    borderWidth: 0
                }]
            },
            options: this.defaultOptions
        });
    },

    // Create line chart for trends
    createTrendChart(ctx, data) {
        return new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Amount',
                    data: data.values,
                    borderColor: '#FFD700',
                    backgroundColor: 'rgba(255, 215, 0, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                ...this.defaultOptions,
                scales: {
                    y: {
                        ticks: { color: '#FFFFFF' },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    },
                    x: {
                        ticks: { color: '#FFFFFF' },
                        grid: { display: false }
                    }
                }
            }
        });
    },

    // Create bar chart
    createBarChart(ctx, data) {
        return new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Amount',
                    data: data.values,
                    backgroundColor: '#FFD700',
                    borderRadius: 8
                }]
            },
            options: {
                ...this.defaultOptions,
                scales: {
                    y: {
                        ticks: { color: '#FFFFFF' },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    },
                    x: {
                        ticks: { color: '#FFFFFF' },
                        grid: { display: false }
                    }
                }
            }
        });
    }
};

window.ChartHelpers = ChartHelpers;
