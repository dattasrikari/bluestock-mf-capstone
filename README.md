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

## Status
- [x] Day 1: Data ingestion
- [ ] Day 2: Data cleaning + SQL database design (in progress)
- [ ] Day 3: EDA
- [ ] Day 4: Performance analytics
- [ ] Day 5: Dashboard
- [ ] Day 6: Advanced analytics
- [ ] Day 7: Final report

## Author
Datta Srikari — Bluestock Fintech Capstone, 2026
