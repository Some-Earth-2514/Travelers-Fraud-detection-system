import pandas as pd 

fraud_ALAE = []
count_ALAE = 0
for i in range(len(CLAIM_EXPENSE_EST_AMT)):
  # check bodily & multiple 
  # if VEH_PRIMARY_PT_OF_DAMAGE is not none and AUTO_ACCIDENT_DESC is multi 
  # multi by collision cost
  total_legal_fees = 0
  total_legal_fees = BI_CLMT_CNT[i] * 15785 
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'No Damage': total_legal_fees += 0
  else: total_legal_fees += 4698 
  if CLAIM_EXPENSE_EST_AMT[i] > total_legal_fees: 
    fraud_ALAE.append(i)
    count_ALAE += 1
print(fraud_ALAE)
print(count_ALAE)