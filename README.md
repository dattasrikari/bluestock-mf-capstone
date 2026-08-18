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

## Day 1: Project Setup + Data Ingestion 

Set up the project environment and ingested all provided datasets plus live NAV data.

**What was done:**
- Created project folder structure (data/raw, data/processed, notebooks, scripts, sql, dashboard, reports, charts)
- `scripts/data_ingestion.py` — loaded all 10 provided CSV datasets, validated shapes/dtypes
- `scripts/live_nav_fetch.py` — fetched live historical NAV data from the mfapi.in API for 6 real schemes: HDFC Top 100 (125497), SBI Bluechip (119551), ICICI Bluechip (120503), Nippon Large Cap (118632), Axis Bluechip (119092), Kotak Bluechip (120841)
- `scripts/validate_codes.py` — cross-checked all AMFI codes in fund_master against nav_history (0 mismatches found)

**Deliverables:** Project repo initialized on GitHub, `data_ingestion.py`, `live_nav_fetch.py`, `validate_codes.py`, raw CSVs in `data/raw/`

---

## Day 2: Data Cleaning + SQL Database Design 

Cleaned all datasets and built a 5-table SQLite star schema.

**What was done:**
- `scripts/clean_nav.py`, `clean_transactions.py`, `clean_performance.py` — cleaned and validated the 3 core datasets, output to `data/processed/`
- Built SQLite schema (`sql/schema.sql`): `dim_fund`, `fact_nav`, `fact_transactions`, `fact_performance`, `fact_aum`
- `scripts/create_schema.py` and `scripts/load_db.py` — created and loaded the schema into `data/db/bluestock_mf.db` (dim_fund: 40 rows, fact_nav: 64,320 rows, fact_transactions: 32,778 rows, fact_performance: 40 rows, fact_aum: 90 rows)
- Wrote and ran 10 analytical SQL queries (`sql/queries.sql`, `scripts/run_queries.py`)
- Documented all tables and columns in `reports/data_dictionary.md`

**Deliverables:** 3 cleaned CSVs, `bluestock_mf.db`, `schema.sql`, `queries.sql`, `data_dictionary.md`

## Day 3: Exploratory Data Analysis 
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

## Day 4: Performance Analytics 
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

## Day 5: Dashboard Development 

Built an interactive 5-page Power BI dashboard covering the full mutual fund analytics platform.

**Pages:**
- **Industry Overview** — KPI cards (Total AUM, SIP Inflows, Folios, Schemes), AUM growth trend, AUM by AMC
- **Fund Performance** — Fund scorecard, Risk vs Return scatter, NAV vs Benchmark comparison, slicers (fund house, category, plan)
- **Investor Analytics** — Transaction amount by state, SIP/Lumpsum/Redemption split, age group SIP averages, monthly transaction volume, slicers (state, age group, city tier)
- **SIP & Market Trends** — SIP inflow vs Nifty 50 dual-axis chart, category inflows heatmap, top 5 categories by net inflow
- **NAV Detail** (interactive sub-page) — fund-level NAV history, accessible via "View NAV Detail" button from Fund Performance page

**Features:**
- Interactive navigation button (Fund Performance → NAV Detail) with fund selector
- Tooltips enabled across all visuals
- Custom Bluestock branding (logo + themed color palette) on every page
- Built a monthly-aggregated benchmark index table via Power Query to relate SIP inflow data with daily Nifty 50 data

**Deliverables:** `dashboard/bluestock_mf_dashboard.pbix`, `dashboard/Dashboard.pdf`, 4 page PNG exports

## Day 6: Advanced Analytics + Risk Metrics 

Extended the analytics layer with risk metrics, cohort behavior, and a simple recommendation engine.

**Analyses performed (`notebooks/Advanced_Analytics.ipynb`):**
- **Historical VaR & CVaR (95%)** per fund — Small/Mid Cap equity funds carry the highest downside risk (ABSL Small Cap worst at -2.39% VaR)
- **Rolling 90-day Sharpe ratio** for 5 selected funds — reveals Liquid funds persistently underperforming the risk-free rate while Small Cap funds oscillate around/above zero
- **Investor cohort analysis** by first transaction year — tracks investor count, average SIP amount, and category preference per cohort
- **SIP continuity analysis** — flags at-risk investors by transaction gap; recalibrated the brief's fixed 35-day threshold to a relative (top 25%) measure after finding this dataset's actual median SIP gap (64.7 days) made the literal threshold non-informative
- **Fund recommendation engine** (`scripts/recommender.py`) — recommends top 3 funds by Sharpe ratio matched to investor risk appetite (Low/Moderate/High)
- **Sector concentration (HHI)** per equity fund — Axis Bluechip Fund is most concentrated (HHI 0.297)

**Deliverables:** `notebooks/Advanced_Analytics.ipynb`, `reports/var_cvar_report.csv`, `reports/cohort_analysis.csv`, `reports/sip_continuity.csv`,

## Status
- [x] Day 1: Data ingestion
- [x] Day 2: Data cleaning + SQL database design
- [x] Day 3: EDA
- [x] Day 4: Performance analytics
- [x] Day 5: Dashboard
- [x] Day 6: Advanced analytics
- [ ] Day 7: Final report
## Author
Datta Srikari — Bluestock Fintech Capstone, 2026
