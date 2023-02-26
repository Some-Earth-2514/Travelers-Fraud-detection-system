import pandas as pd
# functions for analyzing, cleaning, exploring, and manipulating data.
# "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"

# reads the CSV files and prints them out individually
claim_cleaned = pd.read_csv(r"C:\Users\Samarth\Desktop\Traveler's Case Competition\Data sets\CVS\Claim cleaned.csv")
print(claim_cleaned)

claimant_cleaned = pd.read_csv(r"C:\Users\Samarth\Desktop\Traveler's Case Competition\Data sets\CVS\Claimant "
                               r"cleaned.csv")
print(claimant_cleaned)
