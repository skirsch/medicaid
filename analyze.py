#!/usr/bin/env python3
"""
Analyze Medicaid provider spending by HCPCS_CODE and quarter.
Output: one row per (HCPCS_CODE, type) with quarterly sums.
type: "b" = unique beneficiaries, "e" = events (claims), "s" = spending
"""

import pandas as pd

INPUT_FILE = "medicaid-provider-spending.csv"
OUTPUT_FILE = "analysis_output.csv"

# Quarters from Q1 2018 through Q4 2024
QUARTERS = [
    f"Q{q}_{y}"
    for y in range(2018, 2025)
    for q in range(1, 5)
]

def month_to_quarter(month_str: str) -> str:
    """Convert YYYY-MM to Qn_YYYY."""
    year, month = map(int, month_str.split("-"))
    q = (month - 1) // 3 + 1
    return f"Q{q}_{year}"

def main():
    print("Reading data...")
    df = pd.read_csv(
        INPUT_FILE,
        usecols=["HCPCS_CODE", "CLAIM_FROM_MONTH", "TOTAL_UNIQUE_BENEFICIARIES", "TOTAL_CLAIMS", "TOTAL_PAID"],
        dtype={"HCPCS_CODE": str, "CLAIM_FROM_MONTH": str},
        low_memory=False,
    )

    print("Aggregating by code and quarter...")
    df["quarter"] = df["CLAIM_FROM_MONTH"].apply(month_to_quarter)
    df = df[df["quarter"].isin(QUARTERS)]

    g = df.groupby(["HCPCS_CODE", "quarter"]).agg(
        beneficiaries=("TOTAL_UNIQUE_BENEFICIARIES", "sum"),
        events=("TOTAL_CLAIMS", "sum"),
        spending=("TOTAL_PAID", "sum"),
    ).reset_index()

    # Pivot to wide format: one row per (HCPCS_CODE, type)
    codes = g["HCPCS_CODE"].unique()
    out_rows = []
    for code in sorted(codes):
        sub = g[g["HCPCS_CODE"] == code].set_index("quarter")
        for t, col in [("b", "beneficiaries"), ("e", "events"), ("s", "spending")]:
            row = {"HCPCS_CODE": code, "type": t}
            for q in QUARTERS:
                row[q] = sub.loc[q, col] if q in sub.index else 0
            out_rows.append(row)

    df = pd.DataFrame(out_rows, columns=["HCPCS_CODE", "type"] + QUARTERS)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Wrote {len(df)} rows to {OUTPUT_FILE}")
    print(df.head(10).to_string())

if __name__ == "__main__":
    main()
