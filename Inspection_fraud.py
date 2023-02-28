import pandas as pd 

fraud_inspections = []
count_inspections = 0
for i in range(len(APPR_DAM_EST_REC_CNT)):
  if APPR_DAM_EST_REC_CNT[i] > 4:
      fraud_inspections.append(i)
      count_inspections += 1
print(fraud_inspections)
print(count_inspections)