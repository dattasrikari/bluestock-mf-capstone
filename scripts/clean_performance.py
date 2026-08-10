import pandas as pd

perf = pd.read_csv("data/raw/07_scheme_performance.csv", dtype={"amfi_code": str})
print("Columns:", perf.columns.tolist())

numeric_cols = ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct",
                 "sharpe_ratio", "sortino_ratio", "alpha", "beta",
                 "std_dev_ann_pct", "max_drawdown_pct"]

for col in numeric_cols:
    if col in perf.columns:
        non_numeric = pd.to_numeric(perf[col], errors="coerce").isna().sum()
        print(f"{col}: {non_numeric} non-numeric values")

if "sharpe_ratio" in perf.columns:
    print(f"Funds with negative Sharpe ratio: {(perf['sharpe_ratio'] < 0).sum()}")

print("Final shape:", perf.shape)
perf.to_csv("data/processed/clean_performance.csv", index=False)