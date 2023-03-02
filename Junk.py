import main
import csv


def junk():
    junk_sorted = sorted(index + 1 for index in main.junk_initial)
    print(junk_sorted)

    # Read in the input file and remove the specified rows
    with open("Claim.csv", 'r') as f_in_claim, open("Claim_cleaned.csv", 'w', newline='') as f_out_junk:
        reader = csv.reader(f_in_claim)
        writer = csv.writer(f_out_junk)
        for i, row in enumerate(reader):
            if i not in junk_sorted:
                writer.writerow(row)

    with open("Claimant.csv", 'r') as f_in_claim, open("Claimant_cleaned.csv", 'w', newline='') as f_out_junk:
        reader = csv.reader(f_in_claim)
        writer = csv.writer(f_out_junk)
        for i, row in enumerate(reader):
            if i not in junk_sorted:
                writer.writerow(row)

    return junk_sorted
