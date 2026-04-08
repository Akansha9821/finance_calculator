# FinCalc Lib 

A lightweight Python library for essential finance analytics, including NPS, profitability margins, and cash flow metrics.

##### Features

- **Customer Metrics**: Calculate Net Promoter Score (NPS).
- **Profitability**: Gross, Operating, and Net Profit Margins.
- **Liquidity & Leverage**: Current Ratio and Debt-to-Equity.
- **Cash Flow**: Free Cash Flow (FCF) and Operating Cash Flow (CFO).

#### Live URL
https://pypi.org/project/fincalc-lib/

#### Dashboard Image Refrence

https://pypi.org/project/fincalc-lib/

#### List Of All calculated Function and Formulas

<img width="1153" height="638" alt="Screenshot 2026-04-08 at 10 03 49 AM" src="https://github.com/user-attachments/assets/304c5ae0-91d2-4fe3-9168-dc2cf410a35e" />



## Installation
You can install the package directly from PyPI:

```bash
pip install fincalc-lib

Or install the wheel file locally:

pip install fincalc_lib-1.0.0-py3-none-any.whl

## Quick Start
Here is a simple example of how to use the library:

import fincalc
# Calculate Net Promoter Score# Parameters: (promoters, detractors, total_responses)nps = fincalc.calculate_nps(80, 10, 100)
print(f"Your NPS is: {nps}")
# Calculate Profit Margin# Parameters: (profit, revenue)margin = fincalc.profit_margin(20000, 100000)
print(f"Profit Margin: {margin}%")

## Available Formulas
|-----------|---------------------|--------------------------------------|
| Category  | Function            | Formula                              |
|-----------|---------------------|--------------------------------------|
| Customer  | calculate_nps       | %Promoters - %Detractors             |
| Profit    | gross_profit_margin | (Gross Profit / Revenue) * 100       |
| Leverage  | debt_to_equity      | Total Liability / Total Equity       |
| Cash Flow | free_cash_flow      | CFO - Capital Expenditures           |
|-----------|---------------------|--------------------------------------|


## Development
If you want to contribute or build the wheel yourself:

   1. Clone the repo:
   
   git clone [https://github.com](https://github.com/Akansha9821/finance_calculator.git)
   
   2. Build the package:
   
   python -m build
   
   
## License
MIT

