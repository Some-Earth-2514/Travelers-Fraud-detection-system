import main

expense = []

count = 0
# counts how many entries of one are greater than two
for col in range(len(main.CLAIM_EXPENSE_EST_AMT)):
    if main.CLAIM_EXPENSE_EST_AMT[col] > main.CLAIM_INDEMNITY_EST_AMT[col]:
        count += 1
        expense.append(col)
print(count)
print(expense)
