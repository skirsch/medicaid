#!/usr/bin/env python3
"""Summarize Medicaid records by month and procedure code."""

import pandas as pd

# Load records
df = pd.read_csv("records.csv", low_memory=False)

# Parse claim month for proper datetime index
df["CLAIM_FROM_MONTH"] = pd.to_datetime(df["CLAIM_FROM_MONTH"], format="%Y-%m")

# Group by service date (month) and procedure code (HCPCS_CODE)
# Aggregate: sum of unique beneficiaries and sum of claims
summary = (
    df.groupby([df["CLAIM_FROM_MONTH"].dt.to_period("M"), "HCPCS_CODE"])
    .agg(
        total_unique_beneficiaries=("TOTAL_UNIQUE_BENEFICIARIES", "sum"),
        total_claims=("TOTAL_CLAIMS", "sum"),
    )
    .reset_index()
)

# Set multi-index: CLAIM_FROM_MONTH, HCPCS_CODE
summary = summary.set_index(["CLAIM_FROM_MONTH", "HCPCS_CODE"])

# Sort for readability
summary = summary.sort_index()

print(summary.head(50))
print(f"\n... ({len(summary)} rows total)")
print(f"\nOutput saved to summary_by_month_code.csv")
summary.to_csv("summary_by_month_code.csv")
