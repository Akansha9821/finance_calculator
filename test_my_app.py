# test_my_app.py
import fincalc

print("--- Testing Finance Analytics Library ---")

# 1. Test NPS
nps = fincalc.calculate_nps(promoters=80, detractors=10, total_responses=100)
print(f"NPS Score (Expected 70): {nps}")

# 2. Test Profit Margin
margin = fincalc.profit_margin(profit=20000, revenue=100000)
print(f"Profit Margin (Expected 20%): {margin}%")

# 3. Test Debt-to-Equity
ratio = fincalc.debt_to_equity(total_liability=50000, total_equity=100000)
print(f"Debt-to-Equity (Expected 0.5): {ratio}")

# 4. Test Free Cash Flow
fcf = fincalc.free_cash_flow(cfo=5000, capital_expenditures=1200)
print(f"Free Cash Flow (Expected 3800): {fcf}")
