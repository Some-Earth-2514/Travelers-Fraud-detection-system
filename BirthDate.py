import pandas as pd
import datetime as dt
import main


def birth_date():  # done
    # counters for ages below 18 and above 80
    count_birth_date_junk = 0
    count_birth_date_clean = 0
    junk_birth_date = []  # list holding index val. of fraud detected birthday
    clean_birth_date = []

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
            count_birth_date_junk += 1  # 47
            junk_birth_date.append(i)
        else:
            count_birth_date_clean += 1
            clean_birth_date.append(i)

    main.junk_initial.update(junk_birth_date)
    main.clean_initial.update(clean_birth_date)

    print(count_birth_date_junk)
    print(f"Below 18: {junk_birth_date}")
    print(junk_birth_date)
    print(main.junk_initial)

    print(count_birth_date_clean)
    print(f"Above 18: {junk_birth_date}")
    print(clean_birth_date)
    print(main.clean_initial)

    return birth_date
