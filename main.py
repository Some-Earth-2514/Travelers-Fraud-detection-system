import pandas as pd
import datetime as dt
import csv

# def CTL():
# reading CSV file
claim = pd.read_csv("Claim.csv")
claimant = pd.read_csv("Claimant.csv")

claim_cleaned = pd.read_csv("Claim_cleaned.csv")
# claimant_cleaned = pd.read_csv("Claimant_cleaned.csv")

dict_claim = csv.DictReader(claim)
dict_claimant = csv.DictReader(claimant)

csv_claim = csv.reader("Claim.csv")
csv_claimant = csv.reader("Claimant.csv")
print(csv_claim)

# converting column data to list for uncleaned data
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

# converting column data to list for cleaned data
CLM_NBR_c = claim_cleaned['CLM_NBR'].tolist()
NBR_OF_CLMT_c = claim_cleaned['NBR_OF_CLMT'].tolist()
BI_CLMT_CNT_c = claim_cleaned['BI_CLMT_CNT'].tolist()
COV_RGST_DT_c = claim_cleaned['COV_RGST_DT'].tolist()
CLAIM_EXPENSE_EST_AMT_c = claim_cleaned['CLAIM_EXPENSE_EST_AMT'].tolist()
CLAIM_INDEMNITY_EST_AMT_c = claim_cleaned['CLAIM_INDEMNITY_EST_AMT'].tolist()
POL_NBR_c = claim_cleaned['POL_NBR'].tolist()
POLICY_STATE_c = claim_cleaned['POLICY_STATE'].tolist()
PRI_BTH_DT_c = claim_cleaned['PRI_BTH_DT'].tolist()

# CLM_NBR = claimant['CLM_NBR'].tolist()
# AUTO_ACCIDENT_DESC_c = claimant_cleaned['AUTO_ACCIDENT_DESC'].tolist()
# CLAIMANT_STATUS_c = claimant_cleaned['CLAIMANT_STATUS'].tolist()
# APPR_DAM_EST_REC_CNT_c = claimant_cleaned['APPR_DAM_EST_REC_CNT'].tolist()
# VEH_COLR_TXT_c = claimant_cleaned['VEH_COLR_TXT'].tolist()
# VEH_DAM_TXT_c = claimant_cleaned['VEH_DAM_TXT'].tolist()
# CLMT_VEH_MDL_NM_c = claimant['CLMT_VEH_MDL_NM'].tolist()
# CLMT_VEH_YR_c = claimant_cleaned['CLMT_VEH_YR'].tolist()
# VEH_TYPE_c = claimant_cleaned['VEH_TYPE'].tolist()
# VEH_PRIMARY_PT_OF_DAMAGE_c = claimant_cleaned['VEH_PRIMARY_PT_OF_DAMAGE'].tolist()
# AIRBAG_DEPLOYED_c = claimant_cleaned['AIRBAG_DEPLOYED'].tolist()
# VEH_SPEED_AT_IMPACT_c = claimant_cleaned['VEH_SPEED_AT_IMPACT'].tolist()

clean_initial = set()
fraud_initial = set()


def read_datasets():
    pass


def print_datasets():
    pass


def policy_state():  # done
    # appends the index of list 'POLICY_STATE' that is tested when counts are indexed
    clean_policy_state = []
    count_policy_state_clean = 0

    # create a pandas Series from the list 'a'
    series_a = pd.Series(POLICY_STATE)

    # apply pd.to_numeric() with errors='coerce' to convert non-numeric values to NaN
    numeric_series = series_a.apply(pd.to_numeric, errors='coerce')

    # apply notnull() to return a boolean series indicating which values are not null
    count = numeric_series.notnull()

    # iterates through count & check if true
    for i in range(len(count)):
        if count[i]:
            count_policy_state_clean += 1
            clean_policy_state.append(i)

    clean_initial.update(clean_policy_state)

    print(count_policy_state_clean)
    print(clean_policy_state)
    print(clean_initial)

    return policy_state


def birth_date():  # done
    # counters for ages below 18 and above 80
    count_birth_date_junk = 0
    junk_birth_date = []  # list holding index val. of fraud detected birthday

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
            count_birth_date_junk += 1  # 47
            junk_birth_date.append(i)

    clean_initial.update(junk_birth_date)

    print(count_birth_date_junk)
    print(f"Below 18: {junk_birth_date}")
    print(junk_birth_date)
    print(clean_initial)

    return birth_date


def vehicle_year():  # done
    junk_vehicle_year = []

    count_vehicle_year_junk = 0

    # counts how many entries of one are greater than two
    for col in range(len(CLMT_VEH_YR)):
        if CLMT_VEH_YR[col] == 1900:
            count_vehicle_year_junk += 1
            junk_vehicle_year.append(col)

    clean_initial.update(junk_vehicle_year)

    print(count_vehicle_year_junk)
    print(junk_vehicle_year)
    print(clean_initial)

    return vehicle_year


def clean():
    clean_sorted = sorted(index + 1 for index in clean_initial)
    print(clean_sorted)

    # Read in the input file and remove the specified rows
    with open("Claim.csv", 'r') as f_in_claim, open("Claim_cleaned.csv", 'w', newline='') as f_out_clean:
        reader = csv.reader(f_in_claim)
        writer = csv.writer(f_out_clean)
        for i, row in enumerate(reader):
            if i not in clean_sorted:
                writer.writerow(row)

    return clean_sorted


def alea_fraud():
    fraud_ALAE = []
    count_ALAE = 0
    total_legal_fees = 0

    for i in range(len(CLAIM_EXPENSE_EST_AMT_c)):
        # check bodily & multiple
        # if VEH_PRIMARY_PT_OF_DAMAGE is not none and AUTO_ACCIDENT_DESC is multi
        # multi by collision cost
        total_legal_fees = BI_CLMT_CNT_c[i] * 15785
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'No Damage':
            total_legal_fees += 0
        else:
            total_legal_fees += 4698
        if CLAIM_EXPENSE_EST_AMT[i] > total_legal_fees:
            fraud_ALAE.append(i)
            count_ALAE += 1

    fraud_initial.update(fraud_ALAE)

    print(count_ALAE)
    print(fraud_ALAE)
    print(fraud_initial)

    return alea_fraud


def indemnity_fraud():
    fraud_indemity = []
    count = 0

    for i in range(len(CLAIM_INDEMNITY_EST_AMT)):
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'All Over':
            if CLAIM_INDEMNITY_EST_AMT[i] > 118258.5:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Complete Drivers Side':
            if CLAIM_INDEMNITY_EST_AMT[i] > 49868.75:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Complete Front End':
            if CLAIM_INDEMNITY_EST_AMT[i] > 73086.5:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Complete Passenger Side':
            if CLAIM_INDEMNITY_EST_AMT[i] > 85506.50:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Complete Rear End':
            if CLAIM_INDEMNITY_EST_AMT[i] > 19917.5:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Drivers Center':
            if CLAIM_INDEMNITY_EST_AMT[i] > 83830.5:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Driver Front Corner':
            if CLAIM_INDEMNITY_EST_AMT[i] > 61479.75:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Driver Rear Corner':
            if CLAIM_INDEMNITY_EST_AMT[i] > 46557.5:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'No Damage':
            if CLAIM_INDEMNITY_EST_AMT[i] > 16612.5:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Passenger Center':
            if CLAIM_INDEMNITY_EST_AMT[i] > 58335.5:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Passenger Front Corner':
            if CLAIM_INDEMNITY_EST_AMT[i] > 48570.5:
                fraud_indemity.append(i)
        if VEH_PRIMARY_PT_OF_DAMAGE[i] == 'Passenger Rear Corner':
            if CLAIM_INDEMNITY_EST_AMT[i] > 46471.5:
                fraud_indemity.append(i)

    for i in fraud_indemity:
        count += 1

    fraud_initial.update(fraud_indemity)

    print(count)
    print(fraud_indemity)
    print(fraud_initial)

    return indemnity_fraud


def inspection_fraud():
    fraud_inspections = []
    count_inspections = 0

    for i in range(len(APPR_DAM_EST_REC_CNT)):
        if APPR_DAM_EST_REC_CNT[i] > 4:
            fraud_inspections.append(i)
            count_inspections += 1

    fraud_initial.update(fraud_inspections)

    print(count_inspections)
    print(fraud_inspections)
    print(fraud_initial)


def fraud():
    fraud_sorted = sorted(index + 1 for index in fraud_initial)
    print(fraud_sorted)

    # Read in the input file and remove the specified rows
    with open("Claim_cleaned.csv", 'r') as f_in_claim_c, open("Fraud_found.csv", 'w', newline='') as f_out_fraud:
        reader = csv.reader(f_in_claim_c)
        writer = csv.writer(f_out_fraud)
        for i, row in enumerate(reader):
            if i not in fraud_sorted:
                writer.writerow(row)

    return fraud_sorted


def not_fraud():
    pass


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

    print("Clean")
    clean()
    print()

    print("ALEA fraud")
    alea_fraud()
    print()

    print("Indemnity fraud")
    indemnity_fraud()
    print()

    print("Inspection fraud")
    inspection_fraud()
    print()

    print("Fraud")
    fraud()
    print()
