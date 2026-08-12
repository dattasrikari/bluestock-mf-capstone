# Bluestock Fintech — Mutual Fund Analytics Platform

Capstone project: an end-to-end data engineering, ETL pipeline, and analytics
platform for Indian mutual fund data, built for Bluestock Fintech.

## Project Overview
Ingests publicly available AMFI India / mfapi.in data, cleans and loads it into
a SQLite database, computes fund performance & risk metrics (Sharpe, Sortino,
Alpha, Beta), and presents insights via an interactive dashboard.

## Data Sources
- AMFI India (amfiindia.com) — NAV, AUM, folio, SIP data
- mfapi.in — live historical NAV API
- NSE/BSE — benchmark index data

## Project Structure
data/raw/ - original source CSVs + live-fetched NAV data
data/processed/ - cleaned datasets
data/db/ - SQLite database
scripts/ - ETL and analytics scripts
sql/ - schema + queries
notebooks/ - EDA and analysis notebooks
dashboard/ - Power BI / Tableau dashboard files
reports/ - final report and presentation

## How to Run
1. Create a virtual environment and install dependencies:
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
2. Run the ETL pipeline:
   python scripts/data_ingestion.py
   python scripts/live_nav_fetch.py
   python scripts/clean_nav.py

## Exploratory Data Analysis (Day 3)
Full EDA notebook: `notebooks/EDA_Analysis.ipynb`. Charts exported to `charts/`.

**Key findings**
- NAV growth is broad-based across nearly all 40 schemes from 2022–2026, despite the 2024 correction period
- SBI Mutual Fund dominates AUM (~₹12.5L Cr), ~40% higher than second-place ICICI Prudential
- SIP inflows hit an all-time high in Dec 2025 at ₹31,002 Cr
- Liquid funds dominate category-wise net inflows every month, 3-4x higher than other categories
- 26-35 age group makes up 41.1% of investors, but the 56+ group has the highest median SIP amount
- T30 (top 30) cities dominate mutual fund transaction volume, reflecting urban concentration
- Folio count nearly doubled from 13.26 Cr to 26.12 Cr (Jan 2022–Dec 2025)
- Fund NAV returns show near-zero correlation across the 10 selected schemes
- Banking, IT, and Pharma are the top 3 sector exposures, ~45% of holdings combined
- Heavy Liquid-fund inflows + low fund correlation suggest cautious, short-term capital parking rather than long-term equity conviction

## Performance Analytics (Day 4)
Full analytics notebook: `notebooks/Performance_Analytics.ipynb`. Deliverables saved to `reports/`.

**Metrics computed for all 40 funds:**
- Daily returns (validated — 0 outlier days beyond ±20%, clean series)
- CAGR for 1yr, 3yr, and 5yr horizons
- Sharpe Ratio (Rf = 6.5% RBI repo rate proxy) — top fund: Mirae Asset Large Cap (1.07)
- Sortino Ratio (downside deviation only) — top fund: Mirae Asset Large Cap (1.49)
- Alpha and Beta via OLS regression against Nifty 100 — r² near zero across all funds, indicating the dataset's fund NAVs move largely independently of the benchmark (consistent with the near-zero fund-to-fund correlation found in Day 3 EDA)
- Maximum Drawdown — Small/Mid Cap funds show the deepest declines (e.g. SBI Small Cap Fund at -52.6%)
- Composite Fund Scorecard (0–100), weighted by 3yr return, Sharpe, Alpha, expense ratio, and max drawdown — top fund: **Mirae Asset Large Cap Fund** (score: 86.25)
- Benchmark comparison chart — top 5 funds vs Nifty 50 / Nifty 100 over 3 years, all five funds substantially outperform both indices
- Tracking error for top 5 funds — ranges 19–23%, confirming low correlation to the benchmark

**Deliverables:**
- `reports/fund_scorecard.csv`
- `reports/alpha_beta.csv`
- `reports/tracking_error.csv`
- `charts/benchmark_comparison_top5.png`

## Status
- [x] Day 1: Data ingestion
- [x] Day 2: Data cleaning + SQL database design
- [x] Day 3: EDA
- [x] Day 4: Performance analytics
- [ ] Day 5: Dashboard
- [ ] Day 6: Advanced analytics
- [ ] Day 7: Final report
## Author
Datta Srikari — Bluestock Fintech Capstone, 2026
