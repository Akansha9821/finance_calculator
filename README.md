This updated `README.md` incorporates the new advanced analytical features (NPV, EBITDA, Risk Analysis, and Simulations) while maintaining your existing structure and branding.


-----

# FinCalc Lib

A lightweight Python library for essential finance analytics, ranging from basic profitability metrics to advanced risk simulations and time-value-of-money calculations.

##### Features

  - **Customer Metrics**: Calculate Net Promoter Score (NPS).
  - **Profitability**: Gross, Operating, Net Profit Margins, and **EBITDA/EBITA**.
  - **Liquidity & Leverage**: Current Ratio, Debt-to-Equity, and **Return on Equity (ROE)**.
  - **Cash Flow**: Free Cash Flow (FCF), Operating Cash Flow (CFO), and Cash Flow Margin.
  - **Investment Analytics**: **Net Present Value (NPV)** and **Future Value (FV)**.
  - **Risk & Simulation**: **Sharpe Ratio** and **Monte Carlo Price Simulations**.
  - **Compliance**: Built-in audit logging for financial reporting integrity.

#### Live URL

[https://pypi.org/project/fincalc-lib/](https://pypi.org/project/fincalc-lib/)

#### Dashboard Image Reference

[https://pypi.org/project/fincalc-lib/](https://pypi.org/project/fincalc-lib/)

#### List Of All calculated Function and Formulas

\<img width="1153" height="638" alt="FinCalc Dashboard Reference" src="[https://github.com/user-attachments/assets/304c5ae0-91d2-4fe3-9168-dc2cf410a35e](https://github.com/user-attachments/assets/304c5ae0-91d2-4fe3-9168-dc2cf410a35e)" /\>

-----

## Installation

You can install the package directly from PyPI:

```bash
pip install fincalc-lib
```

Or install the wheel file locally:

```bash
pip install fincalc_lib-1.0.0-py3-none-any.whl
```

-----

## Quick Start

Here is a simple example of how to use the library's basic and advanced functions:

```python
import fincalc

# 1. Calculate NPS
nps = fincalc.calculate_nps(80, 10, 100)
print(f"Your NPS is: {nps}")

# 2. Calculate Profit Margin
margin = fincalc.profit_margin(20000, 100000)
print(f"Profit Margin: {margin}%")

# 3. Advanced: Net Present Value (NPV)
# Initial investment of -1000, followed by cash flows of 300, 400, 500 at 5% rate
cash_flows = [-1000, 300, 400, 500]
npv = fincalc.calculate_npv(0.05, cash_flows)
print(f"Investment NPV: {npv:.2f}")

# 4. Advanced: Monte Carlo Simulation
# Predict stock price in 30 days with 10% return and 20% volatility
sim = fincalc.monte_carlo_simulation(start_price=150, days=30, mu=0.1, sigma=0.2)
print(f"Projected Median Price: {sim['median_final_price']:.2f}")
```

-----

## Available Formulas

| Category | Function | Formula |
| :--- | :--- | :--- |
| **Customer** | `calculate_nps` | %Promoters - %Detractors |
| **Profitability** | `ebitda` | Net Income + Interest + Taxes + Depr + Amort |
| **Leverage** | `debt_to_equity` | Total Liability / Total Equity |
| **Leverage** | `return_on_equity` | (Net Income / Avg. Equity) \* 100 |
| **Cash Flow** | `free_cash_flow` | CFO - Capital Expenditures |
| **Investment** | `calculate_npv` | Σ (Cash Flow / (1 + r)^t) |
| **Risk** | `sharpe_ratio` | (Mean Return - Risk Free Rate) / Std Dev |
| **Simulation** | `monte_carlo` | Geometric Brownian Motion Price Paths |

-----

## Development

If you want to contribute or build the wheel yourself:

1.  **Clone the repo:**

    ```bash
    git clone https://github.com/Akansha9821/finance_calculator.git
    ```

2.  **Build the package:**

    ```bash
    python -m build
    ```

## License


MIT
