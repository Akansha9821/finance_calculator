# fincalc/analytics.py
import numpy as np

# --- Compliance & Utility ---
def audit_log(func):
    """Decorator to ensure compliance by logging function inputs and outputs."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # In a real package, you might log this to a file or database
        # print(f"[AUDIT] {func.__name__} called with {args}, {kwargs}. Result: {result}")
        return result
    return wrapper

# --- Customer Metrics ---
@audit_log
def calculate_nps(promoters, detractors, total_responses):
    """NPS = %Promoters - %Detractors"""
    if total_responses == 0: return 0
    p_pct = (promoters / total_responses) * 100
    d_pct = (detractors / total_responses) * 100
    return p_pct - d_pct

# --- Revenue & Profit ---
def net_revenue(total_sales, returns, discounts, allowances):
    return total_sales - returns - discounts - allowances

def net_income(total_revenue, total_expenses):
    return total_revenue - total_expenses

def gross_profit(revenue, cogs):
    return revenue - cogs

def operating_profit(gross_profit, operating_expenses):
    return gross_profit - operating_expenses

@audit_log
def ebita(net_income, interest, taxes, amortization):
    """Earnings Before Interest, Taxes, and Amortization."""
    return net_income + interest + taxes + amortization

@audit_log
def ebitda(net_income, interest, taxes, depreciation, amortization):
    """Earnings Before Interest, Taxes, Depreciation, and Amortization."""
    return net_income + interest + taxes + depreciation + amortization

# --- Efficiency Margins ---
def profit_margin(profit, revenue):
    return (profit / revenue) * 100 if revenue != 0 else 0

def gross_profit_margin(gross_profit, total_revenue):
    return (gross_profit / total_revenue) * 100 if total_revenue != 0 else 0

def operating_margin(operating_income, revenue):
    return (operating_income / revenue) * 100 if revenue != 0 else 0

def net_profit_margin(net_profit, total_revenue):
    return (net_profit / total_revenue) * 100 if total_revenue != 0 else 0

# --- Liquidity & Leverage ---
@audit_log
def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities if current_liabilities != 0 else 0

@audit_log
def debt_to_equity(total_liability, total_equity):
    return total_liability / total_equity if total_equity != 0 else 0

@audit_log
def return_on_equity(net_income, avg_shareholder_equity):
    return (net_income / avg_shareholder_equity) * 100 if avg_shareholder_equity != 0 else 0

# --- Time Value of Money (TVM) ---
@audit_log
def future_value(pv, rate, periods):
    """Calculates FV = PV * (1 + r)^n"""
    return pv * (1 + rate) ** periods

@audit_log
def calculate_npv(rate, cash_flows):
    """
    Calculates Net Present Value.
    cash_flows: List where index 0 is initial investment (negative).
    """
    return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))

# --- Cash Flow ---
def cash_flow_from_operations(net_income, non_cash_expenses, change_in_wc):
    return net_income + non_cash_expenses + change_in_wc

def free_cash_flow(cfo, capital_expenditures):
    return cfo - capital_expenditures

def cash_flow_margin(cfo, revenue):
    return (cfo / revenue) * 100 if revenue != 0 else 0

# --- Risk Analysis & Simulation ---
@audit_log
def sharpe_ratio(returns, risk_free_rate):
    """Measures risk-adjusted return."""
    return (np.mean(returns) - risk_free_rate) / np.std(returns)

def monte_carlo_simulation(start_price, days, mu, sigma, simulations=1000):
    """
    Simulates future price paths using Geometric Brownian Motion.
    mu: expected annual return
    sigma: annual volatility
    """
    dt = 1 / 252  # Trading days in a year
    results = []
    for _ in range(simulations):
        price_path = [start_price]
        for _ in range(days):
            # Price change formula: St = St-1 * exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z)
            drift = (mu - 0.5 * sigma**2) * dt
            shock = sigma * np.sqrt(dt) * np.random.normal()
            price_path.append(price_path[-1] * np.exp(drift + shock))
        results.append(price_path[-1])
    return {
        "mean_final_price": np.mean(results),
        "median_final_price": np.median(results),
        "95_percent_confidence_interval": (np.percentile(results, 2.5), np.percentile(results, 97.5))
    }

# --- Compliance Reporting Placeholder ---
def generate_compliance_report(company_name, metrics_dict):
    """
    Standardizes output for financial reporting.
    """
    report = f"Financial Compliance Report: {company_name}\n"
    report += "="*40 + "\n"
    for key, value in metrics_dict.items():
        report += f"{key.replace('_', ' ').title()}: {value:.2f}\n"
    return report
