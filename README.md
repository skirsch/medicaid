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
`analyze.py` produces the output imported into `analysis.xlsx` (i've removed lines with 0 counts in 2021 to make it smaller). `csv` file as well.

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

# About the codes of interest

These are procedure codes, not ICD10 codes. So this is what they did, not what you have.

Jxxxx
J9022, J1955
Injection/biologic administered
⚠️ High (potential inoculation itself)


86xxx / 82xxx
86022, 86612, 82373
Immune/antibody testing
⚠️ Moderate–High


93xxx (cardiac)
93786, 93788, 93662
Cardiac monitoring
⚠️ Moderate–High (myocarditis)


G04xx / G03xx
G0495, G0496, G0329
Telehealth, care coordination
⚠️ Moderate


Mxxxx
M0150, M0152
OASIS admin
❌ None


V, L, D codes
V2206, L0633, D3348
Prosthetics / vision / dental
❌ None

