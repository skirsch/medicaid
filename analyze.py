#!/usr/bin/env python3
"""
Analyze Medicaid provider spending by HCPCS_CODE and month.
Output: one row per (HCPCS_CODE, type) with monthly sums.
type: "b" = unique beneficiaries, "e" = events (claims), "s" = spending
"""

import pandas as pd

INPUT_FILE = "medicaid-provider-spending.csv"
OUTPUT_FILE = "analysis_output.csv"

# Months from 2018-01 through 2024-12
MONTHS = [
    f"{y}-{m:02d}"
    for y in range(2018, 2025)
    for m in range(1, 13)
]

def main():
    print("Reading data...")
    df = pd.read_csv(
        INPUT_FILE,
        usecols=["HCPCS_CODE", "CLAIM_FROM_MONTH", "TOTAL_UNIQUE_BENEFICIARIES", "TOTAL_CLAIMS", "TOTAL_PAID"],
        dtype={"HCPCS_CODE": str, "CLAIM_FROM_MONTH": str},
        low_memory=False,
    )

    print("Aggregating by code and month...")
    df = df[df["CLAIM_FROM_MONTH"].isin(MONTHS)]

    g = df.groupby(["HCPCS_CODE", "CLAIM_FROM_MONTH"]).agg(
        beneficiaries=("TOTAL_UNIQUE_BENEFICIARIES", "sum"),
        events=("TOTAL_CLAIMS", "sum"),
        spending=("TOTAL_PAID", "sum"),
    ).reset_index()

    # Pivot to wide format: one row per (HCPCS_CODE, type)
    codes = g["HCPCS_CODE"].unique()
    out_rows = []
    for code in sorted(codes):
        sub = g[g["HCPCS_CODE"] == code].set_index("CLAIM_FROM_MONTH")
        for t, col in [("b", "beneficiaries"), ("e", "events"), ("s", "spending")]:
            row = {"HCPCS_CODE": code, "type": t}
            for m in MONTHS:
                row[m] = sub.loc[m, col] if m in sub.index else 0
            out_rows.append(row)

    df = pd.DataFrame(out_rows, columns=["HCPCS_CODE", "type"] + MONTHS)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Wrote {len(df)} rows to {OUTPUT_FILE}")
    print(df.head(10).to_string())

if __name__ == "__main__":
    main()
