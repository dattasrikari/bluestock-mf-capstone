import pandas as pd

tx = pd.read_csv("data/raw/08_investor_transactions.csv", dtype={"amfi_code": str})

print("Before:", tx["transaction_type"].unique())
tx["transaction_type"] = tx["transaction_type"].str.strip().str.title()
tx["transaction_type"] = tx["transaction_type"].replace({
    "Sip": "SIP", "Lump Sum": "Lumpsum"
})
print("After:", tx["transaction_type"].unique())

print(f"Rows with amount <= 0: {(tx['amount_inr'] <= 0).sum()}")
tx = tx[tx["amount_inr"] > 0]

tx["transaction_date"] = pd.to_datetime(tx["transaction_date"], errors="coerce")
print(f"Rows with unparseable dates: {tx['transaction_date'].isna().sum()}")
tx = tx.dropna(subset=["transaction_date"])

print("KYC status values:", tx["kyc_status"].unique())

print("Final shape:", tx.shape)
tx.to_csv("data/processed/clean_transactions.csv", index=False)