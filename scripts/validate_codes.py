import pandas as pd

fm = pd.read_csv("data/raw/01_fund_master.csv", dtype={"amfi_code": str})
fund_codes = set(fm["amfi_code"])

for fname in ["02_nav_history.csv", "07_scheme_performance.csv",
              "08_investor_transactions.csv", "09_portfolio_holdings.csv"]:
    df = pd.read_csv(f"data/raw/{fname}", dtype={"amfi_code": str})
    missing = set(df["amfi_code"]) - fund_codes
    print(f"{fname}: {len(missing)} codes not in fund_master -> {missing}")