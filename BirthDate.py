import pandas as pd
import main
import datetime as dt
# Datetime - supplies classes for manipulating dates and times

# counters for ages below 18 and above 80
count = 0
junk_bd = []  # list holding index val. of fraud detected birthday

# iterate through the PRI_BTH_DT colm
for i in range(len(main.PRI_BTH_DT)):
    # person's birthdate in datetime format
    bd = pd.to_datetime(main.PRI_BTH_DT[i])
    # current datetime
    current_dt = pd.to_datetime(dt.date.today())
    current_age = (current_dt - bd) // pd.Timedelta(days=365.25)  # calculating age
    # print(current_age)
    # looping through for checking age bounds
    # total = 47
    if current_age < 18:
        count += 1  # 47
        junk_bd.append(i)

main.junk.update(junk_bd)

print(f"Below 18: {count}")
print(main.junk)
