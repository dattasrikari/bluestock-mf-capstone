"""
Fund recommendation logic for Bluestock Fintech MF Analytics Platform.
Given an investor's risk appetite, recommends top N funds by Sharpe ratio
within matching risk category.
"""

import pandas as pd
from pathlib import Path

REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

# Map brief's 3-tier input to the dataset's actual 5 risk_category values
RISK_MAP = {
    "Low": ["Low"],
    "Moderate": ["Moderate", "Moderately High"],
    "High": ["High", "Very High"]
}


def load_data():
    fund_scorecard = pd.read_csv(REPORTS_DIR / "fund_scorecard.csv")
    fund_master = pd.read_csv(RAW_DIR / "01_fund_master.csv")
    scorecard_with_risk = fund_scorecard.merge(
        fund_master[["amfi_code", "risk_category"]], on="amfi_code"
    )
    return scorecard_with_risk


def recommend_funds(risk_appetite: str, top_n: int = 3, data: pd.DataFrame = None):
    """
    Recommend top N funds by Sharpe ratio matching the investor's risk appetite.

    Parameters
    ----------
    risk_appetite : str
        One of 'Low', 'Moderate', or 'High'.
    top_n : int
        Number of funds to return (default 3).
    data : pd.DataFrame, optional
        Pre-loaded scorecard+risk data. If None, loads from disk.

    Returns
    -------
    pd.DataFrame with scheme_name, risk_category, sharpe_ratio, cagr_3yr, fund_score
    """
    if risk_appetite not in RISK_MAP:
        raise ValueError(f"risk_appetite must be one of {list(RISK_MAP.keys())}")

    if data is None:
        data = load_data()

    matching_categories = RISK_MAP[risk_appetite]
    matches = data[data["risk_category"].isin(matching_categories)]
    top_funds = matches.sort_values("sharpe_ratio", ascending=False).head(top_n)

    return top_funds[["scheme_name", "risk_category", "sharpe_ratio", "cagr_3yr", "fund_score"]]


if __name__ == "__main__":
    data = load_data()
    for level in ["Low", "Moderate", "High"]:
        print(f"\n=== Top 3 funds for '{level}' risk appetite ===")
        print(recommend_funds(level, data=data).to_string(index=False))