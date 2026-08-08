import requests
import pandas as pd

schemes = {
    "125497": "HDFC_Top_100",
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_Large_Cap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip",
}

for code, name in schemes.items():
    r = requests.get(f"https://api.mfapi.in/mf/{code}")
    data = r.json()
    df = pd.DataFrame(data["data"])
    df.to_csv(f"data/raw/live_nav_{name}_{code}.csv", index=False)
    print(name, df.shape, df["date"].min(), df["date"].max())