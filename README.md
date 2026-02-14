# The Medicaid data: a very quick analysis

the code and spreadsheet can be found here:
https://github.com/skirsch/medicaid

This only took me about 5 minutes to do. 

AI suggested the codes to look at:
https://alter.systems/p/ad91141f-34cd-44a5-8e10-6761e5b7d113

Isn't it nice to have transparency?

See the AI link for the anlysis of the two highest curves.

for some reason, cardiac screenings went up by 50% almost immediately after the COVID shots rolled out.

I wonder what could cause such massive harm??? Baffling!!

I don't think they will EVER figure this out, will they?

My initial X post shows the graph:
https://x.com/stkirsch/status/2022576525955285173?s=20

See the .xlsx file for the live plot.

## Full analysis file
`analyze.py` produces `analysis_output.csv`

## About the HHS dataset
The HHS data can be downloaded here: https://opendata.hhs.gov/


## Visualization with spending over time
Explorer here: https://www.medicaidopendata.org/ 

## Other githubs
https://github.com/OpenVaet/medicaid/

## The HCPCS code definitions
Level 2 are letter + 4 digits:
https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update 

Level 1 (CPT) are 5 digits:
https://www.cms.gov/medicare/payment/fee-schedules/physician/pfs-relative-value-files/rvu26a

The HCPCS code field includes Level 1, Level 2, ICD10 & Revenue Codes apparently

# to investigate
A0426 is abulance transport non-emergency. It's flat.
A0427 is 911 call. it's up and hasn't returned to baseline
A0433 is is extreme emergeny. Highest‑level paramedic care — multiple IVs, drug injection, advanced airway. These calls are way up and haven't returned to baseline.
