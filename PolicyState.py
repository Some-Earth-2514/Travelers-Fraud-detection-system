import pandas as pd
import main
# import modules

count_null = 0
# iterates through colm policy_state
for column in main.POLICY_STATE:
    # if every instance in the colm is a str, add 1 to counter
    if not isinstance(column, str):
        count_null += 1

# prints null values identified
print(count_null)

count_num = 0
# converts the argument into a numeric type and checks if the value in Nan(null),
# also checks if it's not null and returns True
count = pd.to_numeric(main.claim['POLICY_STATE'], errors='coerce').notnull()
# returns a list of variables
# iterates through count
for i in count:
    if i:
        count_num += 1
# prints int values identified
print(count_num)
