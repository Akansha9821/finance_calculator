# FinCalc Lib 

A lightweight Python library for essential finance analytics, including NPS, profitability margins, and cash flow metrics.

#### Features- **Customer Metrics**: Calculate Net Promoter Score (NPS).- **Profitability**: Gross, Operating, and Net Profit Margins.- **Liquidity & Leverage**: Current Ratio and Debt-to-Equity.- **Cash Flow**: Free Cash Flow (FCF) and Operating Cash Flow (CFO).

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
   
   git clone https://github.com
   
   2. Build the package:
   
   python -m build
   
   
## License
MIT

