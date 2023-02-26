import pandas as pd
import PolicyState as ps

# def CTL():
# reading CSV file
claim = pd.read_csv("Claim cleaned.csv")

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


def read_datasets():
    pass


def print_datasets():
    pass


def columns_to_list():
    pass  # done


def policy_state():
    pass  # done


def claimant_numbers():
    pass


def injured_numbers():
    pass


def birth_date():
    pass


def vehicle_year():
    pass


def airbags():
    pass


def speed():
    pass
