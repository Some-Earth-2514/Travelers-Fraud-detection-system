import pandas as pd
import datetime as dt
import csv

# def CTL():
# reading CSV file
claim = pd.read_csv("Claim cleaned.csv")
claimant = pd.read_csv("Claimant cleaned.csv")
dict_claim = csv.DictReader(claim)
dict_claimant = csv.DictReader(claimant)

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

junk_inital = set()


def read_datasets():
    pass


def print_datasets():
    pass


def fraud():
    pass


def not_fraud():
    pass


def junk():
    sorted_set = sorted(junk_inital)
    print(sorted_set)

    return junk


def policy_state():
    # appends the index of list 'POLICY_STATE' that is tested when counts are indexed
    junk_policy_state = []
    count_num = 0

    # create a pandas Series from the list 'a'
    series_a = pd.Series(POLICY_STATE)

    # apply pd.to_numeric() with errors='coerce' to convert non-numeric values to NaN
    numeric_series = series_a.apply(pd.to_numeric, errors='coerce')

    # apply notnull() to return a boolean series indicating which values are not null
    count = numeric_series.notnull()

    # iterates through count & check if true
    for i in range(len(count)):
        if count[i]:
            count_num += 1
            junk_policy_state.append(i)

    junk_inital.update(junk_policy_state)

    print(count_num)
    print(junk_policy_state)
    print(junk_inital)

    return policy_state


def birth_date():  # done
    # counters for ages below 18 and above 80
    count = 0
    junk_bd = []  # list holding index val. of fraud detected birthday

    # iterate through the PRI_BTH_DT colm
    for i in range(len(PRI_BTH_DT)):
        # person's birthdate in datetime format
        bd = pd.to_datetime(PRI_BTH_DT[i])
        # current datetime
        current_dt = pd.to_datetime(dt.date.today())
        current_age = (current_dt - bd) // pd.Timedelta(days=365.25)  # calculating age
        # print(current_age)
        # looping through for checking age bounds
        # total = 47
        if current_age < 18:
            count += 1  # 47
            junk_bd.append(i)

    junk_inital.update(junk_bd)

    print(f"Below 18: {count}")
    print(junk_bd)
    print(junk_inital)

    return birth_date


def vehicle_year():  # done
    junk_veh_yr = []

    count = 0
    # counts how many entries of one are greater than two
    for col in range(len(CLMT_VEH_YR)):
        if CLMT_VEH_YR[col] == 1900:
            count += 1
            junk_veh_yr.append(col)

    junk_inital.update(junk_veh_yr)

    print(count)
    print(junk_veh_yr)
    print(junk_inital)

    return vehicle_year


if __name__ == "__main__":
    print("Policy state")
    policy_state()
    print()

    print("Birth date")
    birth_date()
    print()

    print("Vehicle year")
    vehicle_year()
    print()

    print("Junk")
    junk()
    print()
