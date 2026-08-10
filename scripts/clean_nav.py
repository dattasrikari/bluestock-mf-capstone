import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv", dtype={"amfi_code": str})

# Parse dates — no dayfirst assumption yet, let's see what format it actually needs
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")
print(f"Rows with unparseable dates: {nav['date'].isna().sum()}")
nav = nav.dropna(subset=["date"])

before = len(nav)
nav = nav.drop_duplicates(subset=["amfi_code", "date"])
print(f"Removed {before - len(nav)} duplicate rows")

print(f"Rows with NAV <= 0: {(nav['nav'] <= 0).sum()}")
nav = nav[nav["nav"] > 0]

nav = nav.sort_values(["amfi_code", "date"])

# Forward-fill missing calendar days, per fund, using a simple loop
filled_frames = []
for code, group in nav.groupby("amfi_code"):
    g = group.set_index("date")
    full_range = pd.date_range(g.index.min(), g.index.max(), freq="D")
    g = g.reindex(full_range)
    g["nav"] = g["nav"].ffill()
    g["amfi_code"] = code
    g.index.name = "date"
    filled_frames.append(g.reset_index())

nav_filled = pd.concat(filled_frames, ignore_index=True)
print("Final shape:", nav_filled.shape)
nav_filled.to_csv("data/processed/clean_nav.csv", index=False)
print("Saved to data/processed/clean_nav.csv")