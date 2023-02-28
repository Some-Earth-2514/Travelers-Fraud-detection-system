# importing module
import pandas as pd

# reading CSV file
claim = pd.read_csv("claim_small.csv")
claimant = pd.read_csv("claimant_small.csv")

CLM_NBR = claim['CLM_NBR'].tolist()
NBR_OF_CLMT = claim['NBR_OF_CLMT'].tolist()
BI_CLMT_CNT = claim['BI_CLMT_CNT'].tolist()
COV_RGST_DT = claim['COV_RGST_DT'].tolist()
CLAIM_EXPENSE_EST_AMT = claim['CLAIM_EXPENSE_EST_AMT'].tolist()
CLAIM_INDEMNITY_EST_AMT = claim['CLAIM_INDEMNITY_EST_AMT'].tolist()
POL_NBR = claim['POL_NBR'].tolist()
POLICY_STATE = claim['POLICY_STATE'].tolist()
PRI_BTH_DT = claim['PRI_BTH_DT'].tolist()

# CLM_NBR = claimant['CLM_NBR'].tolist()
AUTO_ACCIDENT_DESC = claimant['AUTO_ACCIDENT_DESC'].tolist()
CLAIMANT_STATUS = claimant['CLAIMANT_STATUS'].tolist()
APPR_DAM_EST_REC_CNT = claimant['APPR_DAM_EST_REC_CNT'].tolist()
VEH_COLR_TXT = claimant['VEH_COLR_TXT'].tolist()
VEH_DAM_TXT = claimant['VEH_DAM_TXT'].tolist()
CLMT_VEH_MDL_NM = claimant['CLMT_VEH_MDL_NM'].tolist()
CLMT_VEH_YR = claimant['CLMT_VEH_YR'].tolist()
VEH_TYPE = claimant['VEH_TYPE'].tolist()
VEH_PRIMARY_PT_OF_DAMAGE = claimant['VEH_PRIMARY_PT_OF_DAMAGE'].tolist()
AIRBAG_DEPLOYED = claimant['AIRBAG_DEPLOYED'].tolist()
VEH_SPEED_AT_IMPACT = claimant['VEH_SPEED_AT_IMPACT'].tolist()


## NOTE: check which signifance level was used please/ refind upper and lower bounds and plug in
fraud_indemity = []
for i in range(len(CLAIM_INDEMNITY_EST_AMT)):
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'All Over':
     if CLAIM_INDEMNITY_EST_AMT[i] < -50041.5 or CLAIM_INDEMNITY_EST_AMT[i] > 118258.5: 
      fraud_indemity.append(i)
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Complete Drivers Side':
     if CLAIM_INDEMNITY_EST_AMT[i] < -25953.25 or CLAIM_INDEMNITY_EST_AMT[i] > 49868.75: 
      fraud_indemity.append(i)    
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Complete Front End':
     if CLAIM_INDEMNITY_EST_AMT[i] < -35157.5 or CLAIM_INDEMNITY_EST_AMT[i] > 73086.5: 
      fraud_indemity.append(i)    
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Complete Passenger Side':
     if CLAIM_INDEMNITY_EST_AMT[i] < -46325.50 or CLAIM_INDEMNITY_EST_AMT[i] > 85506.50: 
      fraud_indemity.append(i)    
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Complete Rear End':
     if CLAIM_INDEMNITY_EST_AMT[i] < -11950.5 or CLAIM_INDEMNITY_EST_AMT[i] > 19917.5: 
      fraud_indemity.append(i)    
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Drivers Center':
     if CLAIM_INDEMNITY_EST_AMT[i] < -48941.5 or CLAIM_INDEMNITY_EST_AMT[i] > 83830.5: 
      fraud_indemity.append(i)    
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Driver Front Corner':
     if CLAIM_INDEMNITY_EST_AMT[i] < -33722.25 or CLAIM_INDEMNITY_EST_AMT[i] > 61479.75: 
      fraud_indemity.append(i)   
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Driver Rear Corner':
     if CLAIM_INDEMNITY_EST_AMT[i] < -27726.5 or CLAIM_INDEMNITY_EST_AMT[i] > 46557.5: 
      fraud_indemity.append(i)    
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'No Damage':
     if CLAIM_INDEMNITY_EST_AMT[i] < -8847.5 or CLAIM_INDEMNITY_EST_AMT[i] > 16612.5: 
      fraud_indemity.append(i)   
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Passenger Center':
     if CLAIM_INDEMNITY_EST_AMT[i] < -30364.5 or CLAIM_INDEMNITY_EST_AMT[i] > 58335.5: 
      fraud_indemity.append(i)   
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Passenger Front Corner':
     if CLAIM_INDEMNITY_EST_AMT[i] < -23145.5 or CLAIM_INDEMNITY_EST_AMT[i] > 48570.5: 
      fraud_indemity.append(i)   
  if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Passenger Rear Corner':
     if CLAIM_INDEMNITY_EST_AMT[i] < -26820.5 or CLAIM_INDEMNITY_EST_AMT[i] > 46471.5: 
      fraud_indemity.append(i)   

print(fraud_indemity)