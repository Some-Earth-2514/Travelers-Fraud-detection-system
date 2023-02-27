import csv
import pandas as pd
import main

# CSV - implements classes to read and write tabular data in CSV format
# Pandas - functions for analyzing, cleaning, exploring, and manipulating data.
#          "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"
# NumPy - performs a wide variety of mathematical operations on arrays
# SciPy - provides more utility functions for optimization, stats and signal processing as it's built on NumPy

# opens the file (must be in same directory/folder)
# 'with' is a concise try-catch block and closes resources right after processing them

claim = pd.read_csv("Claim cleaned.csv")

with open('Claim cleaned.csv') as file_obj:

    # Create a reader object by passing the file
    # object to reader method

    # csv.reader() is a read and write sequence
    # preference for small/simple files
    csv_reader = csv.reader(file_obj)

    # DictReader() is a dictionary mapper
    # preference for big/complex files
    dict_reader = csv.DictReader(file_obj)

    # Iterate over each row in the csv
    # file using reader object
    for row in dict_reader:
        print(row)

    # prints the sum of missing values within each column in both files.
    print(main.claim.isnull().sum(), '\n')

    # finds the outliers by using z score
    # claim_outliers = claim[np.abs(stats.zscore(claim.NBR_OF_CLMT)) < 3]

    # find the outliers by using z score
    """claim_z = stats.zscore(ctlp.claim.NBR_OF_CLMT)
    for i in range(claim_z):
        if claim_z > 3:
            i += 1
    print(claim_z)"""
