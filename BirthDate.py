import pandas as pd
import main
import datetime
# Datetime - supplies classes for manipulating dates and times
# counters for ages below 18 and above 80
count_18 = 0
count_80 = 0
junk_ages = [] # list holding index val. of fraud detected birthday

# iterate through the PRI_BTH_DT colm
for i in range(len(main.PRI_BTH_DT)):
    # person's birthdate in datetime format
    birth_date = pd.to_datetime(main.PRI_BTH_DT[i])
    # current datetime
    current_dt = pd.to_datetime(datetime.date.today())
    current_age = (current_dt - birth_date) // pd.Timedelta(days=365.25)  # calculating age
    # print(current_age)
    # looping through for checking age bounds
    # total = 117
    if current_age < 18:
        count_18 += 1  # 47
        junk_ages.append(i) 
    if current_age > 80:  # 70
        count_80 += 1
        junk_ages.append(i)

print(f"Below 18: {count_18}")
print(f"Above 80: {count_80}")
print(junk_ages)