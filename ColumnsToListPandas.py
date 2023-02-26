# importing module
import pandas as pd

# converting data to list & printing 
# reading CSV file
claim = pd.read_csv('Claim_cleaned.csv')

# iterates through columns & printing list data 
for col in ['CLM_NBR', 'NBR_OF_CLMT', 'BI_CLMT_CNT', 'COV_RGST_DT', 'CLAIM_EXPENSE_EST_AMT', 'CLAIM_INDEMNITY_EST_AMT', 'POL_NBR', 'POLICY_STATE', 'PRI_BTH_DT']:
  col_list = claim[col].tolist() # coverting column data to list
  print(f'{col}: {col_list}')