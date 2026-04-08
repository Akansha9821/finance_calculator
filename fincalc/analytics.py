# fincalc/analytics.py

# --- Customer Metrics ---
def calculate_nps(promoters, detractors, total_responses):
    """NPS = %Promoters - %Detractors"""
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

def profit_margin(profit, revenue):
    return (profit / revenue) * 100

# --- Efficiency Margins ---
def gross_profit_margin(gross_profit, total_revenue):
    return (gross_profit / total_revenue) * 100

def operating_margin(operating_income, revenue):
    return (operating_income / revenue) * 100

def net_profit_margin(net_profit, total_revenue):
    return (net_profit / total_revenue) * 100

# --- Liquidity & Leverage ---
def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities

def debt_to_equity(total_liability, total_equity):
    return total_liability / total_equity

def return_on_equity(net_income, avg_shareholder_equity):
    return (net_income / avg_shareholder_equity) * 100

# --- Cash Flow ---
def cash_flow_from_operations(net_income, non_cash_expenses, change_in_wc):
    return net_income + non_cash_expenses + change_in_wc

def free_cash_flow(cfo, capital_expenditures):
    return cfo - capital_expenditures

def cash_flow_margin(cfo, revenue):
    return (cfo / revenue) * 100
