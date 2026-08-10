import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

# --- dim_fund ---
fm = pd.read_csv("data/raw/01_fund_master.csv", dtype={"amfi_code": str})
fm = fm[["amfi_code", "scheme_name", "fund_house", "category", "sub_category",
         "plan", "launch_date", "benchmark", "expense_ratio_pct",
         "exit_load_pct", "fund_manager", "risk_category"]]
fm.to_sql("dim_fund", conn, if_exists="append", index=False)
print("dim_fund loaded:", len(fm), "rows")

# --- fact_nav ---
nav = pd.read_csv("data/processed/clean_nav.csv", dtype={"amfi_code": str})
nav = nav.rename(columns={"date": "nav_date"})
nav = nav[["amfi_code", "nav_date", "nav"]]
nav.to_sql("fact_nav", conn, if_exists="append", index=False)
print("fact_nav loaded:", len(nav), "rows")

# --- fact_transactions ---
tx = pd.read_csv("data/processed/clean_transactions.csv", dtype={"amfi_code": str})
tx = tx.reset_index(drop=True)
tx["tx_id"] = tx.index + 1
tx = tx[["tx_id", "investor_id", "amfi_code", "transaction_date", "amount_inr",
         "transaction_type", "state", "city", "city_tier", "age_group",
         "gender", "payment_mode", "kyc_status"]]
tx.to_sql("fact_transactions", conn, if_exists="append", index=False)
print("fact_transactions loaded:", len(tx), "rows")

# --- fact_performance ---
perf = pd.read_csv("data/processed/clean_performance.csv", dtype={"amfi_code": str})
perf = perf[["amfi_code", "return_1yr_pct", "return_3yr_pct", "return_5yr_pct",
             "sharpe_ratio", "sortino_ratio", "alpha", "beta", "max_drawdown_pct"]]
perf.to_sql("fact_performance", conn, if_exists="append", index=False)
print("fact_performance loaded:", len(perf), "rows")

# --- fact_aum ---
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
aum.to_sql("fact_aum", conn, if_exists="append", index=False)
print("fact_aum loaded:", len(aum), "rows")

conn.close()
print("All tables loaded successfully.")