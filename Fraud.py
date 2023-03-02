import main
import csv


def fraud():
    fraud_sorted = sorted(index + 1 for index in main.fraud_initial)
    print(fraud_sorted)

    # Read in the input file and remove the specified rows
    with open("Claim_cleaned.csv", 'r') as f_in_claim, open("FraudFound_claim.csv", 'w', newline='') as f_out_junk:
        reader = csv.reader(f_in_claim)
        writer = csv.writer(f_out_junk)
        for i, row in enumerate(reader):
            if i in fraud_sorted:
                writer.writerow(row)

    with open("Claimant_cleaned.csv", 'r') as f_in_claim, open("FraudFound_claimant.csv", 'w', newline='') as f_out_junk:
        reader = csv.reader(f_in_claim)
        writer = csv.writer(f_out_junk)
        for i, row in enumerate(reader):
            if i in fraud_sorted:
                writer.writerow(row)

    return fraud_sorted
