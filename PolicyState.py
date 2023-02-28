import main
import pandas as pd

# appends the index of list 'POLICY_STATE' that is tested when counts are indexed
junk_policy_state = []
count_num = 0

# create a pandas Series from the list 'a'
series_a = pd.Series(main.POLICY_STATE)

# apply pd.to_numeric() with errors='coerce' to convert non-numeric values to NaN
numeric_series = series_a.apply(pd.to_numeric, errors='coerce')

# apply notnull() to return a boolean series indicating which values are not null
count = numeric_series.notnull()

# iterates through count & check if true
for i in range(len(count)):
    if count[i]:
        count_num += 1
        junk_policy_state.append(i)


print(count_num)
print(junk_policy_state)
