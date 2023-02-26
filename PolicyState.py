import pandas as pd
import main
# import modules

count_null = 0
# iterates through colm policy_state
for column in main.POLICY_STATE:
    if not isinstance(column, str):
        count_null += 1

integers = [item for item in main.POLICY_STATE if isinstance(item, int)]
# prints null values identified
print(count_null)

count_num = 0
count = pd.to_numeric(main.claim['POLICY_STATE'], errors='coerce').notnull()
# returns a list of variables
# iterates through count
for i in count:
    if i:
        count_num += 1
# prints int values identified
print(count_num)
