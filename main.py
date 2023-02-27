import pandas as pd
import datetime as dt

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


def fraud():
    pass


def not_fraud():
    pass


def policy_state():
    count_null = 0
    # iterates through colm policy_state
    for column in POLICY_STATE:
        if not isinstance(column, str):
            count_null += 1

    integers = [item for item in POLICY_STATE if isinstance(item, int)]
    # prints null values identified
    print("The total number of integer value's in POLICY_STATE is", count_null)

    count_num = 0
    count = pd.to_numeric(claim['POLICY_STATE'], errors='coerce').notnull()
    # returns a list of variables
    # iterates through count
    for i in count:
        if i:
            count_num += 1
    # prints int values identified
    print("The total number of null/blank value's in POLICY_STATE is", count_num)

    return policy_state


def claimant_numbers():
    pass


def injured_numbers():
    pass


def birth_date():
    # counters for ages below 18 and above 80
    count_18 = 0
    count_80 = 0

    # iterate through the PRI_BTH_DT colm
    for i in PRI_BTH_DT:
        # person's birthdate in datetime format
        bd = pd.to_datetime(i)
        # current datetime
        current_dt = pd.to_datetime(dt.date.today())
        current_age = (current_dt - bd) // pd.Timedelta(days=365.25)  # calculating age
        # print(current_age)
        # looping through for checking age bounds
        # total = 117
        if current_age < 18:
            count_18 += 1  # 47
        if current_age > 80:  # 70
            count_80 += 1

    print(f"Below 18: {count_18}")
    print(f"Above 80: {count_80}")

    return birth_date


def expense():
    exp = []

    count = 0
    # counts how many entries of one are greater than two
    for col in range(len(CLAIM_EXPENSE_EST_AMT)):
        if CLAIM_EXPENSE_EST_AMT[col] > CLAIM_INDEMNITY_EST_AMT[col]:
            count += 1
            exp.append(col)
    print(count)
    print(exp)

    return expense


def vehicle_year():
    pass


def airbags():
    pass


def speed():
    pass


if __name__ == "__main__":
    policy_state()
    birth_date()
    expense()
