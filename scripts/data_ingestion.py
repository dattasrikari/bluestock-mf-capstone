from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parent.parent

csv_path = project_root / "data" / "raw" / "01_fund_master.csv"

df = pd.read_csv(csv_path)

print(df.shape)
print(df.dtypes)
print(df.head())