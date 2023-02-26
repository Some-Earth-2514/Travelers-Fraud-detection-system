# importing module
from pandas import *


def ColumnsToListPandas():
    # reading CSV file
    claim = read_csv("Claim cleaned.csv")

    # converting column data to list

    CLM_NBR = claim['CLM_NBR'].tolist()
    NBR_OF_CLMT = claim['NBR_OF_CLMT'].tolist()
    BI_CLMT_CNT = claim['BI_CLMT_CNT'].tolist()
    COV_RGST_DT = claim['COV_RGST_DT'].tolist()
    CLAIM_EXPENSE_EST_AMT = claim['CLAIM_EXPENSE_EST_AMT'].tolist()
    CLAIM_INDEMNITY_EST_AMT = claim['CLAIM_INDEMNITY_EST_AMT'].tolist()
    POL_NBR = claim['POL_NBR'].tolist()
    POLICY_STATE = claim['POLICY_STATE'].tolist()
    PRI_BTH_DT = claim['PRI_BTH_DT'].tolist()

    # printing list data
    print('CLM_NBR:', CLM_NBR)
    print('NBR_OF_CLMT:', NBR_OF_CLMT)
    print('BI_CLMT_CNT:', BI_CLMT_CNT)
    print('COV_RGST_DT:', COV_RGST_DT)
    print('CLAIM_EXPENSE_EST_AMT:', CLAIM_EXPENSE_EST_AMT)
    print('CLAIM_INDEMNITY_EST_AMT:', CLAIM_INDEMNITY_EST_AMT)
    print('POL_NBR:', POL_NBR)
    print('POLICY_STATE:', POLICY_STATE)
    print('PRI_BTH_DT:', PRI_BTH_DT)


print(ColumnsToListPandas())
