import main
import pandas as pd


def policy_state():  # done
    # appends the index of list 'POLICY_STATE' that is tested when counts are indexed
    junk_policy_state = []
    clean_policy_state = []
    count_policy_state_junk = 0
    count_policy_state_clean = 0

    # create a pandas Series from the list 'a'
    series_a = pd.Series(main.POLICY_STATE)

    # apply pd.to_numeric() with errors='coerce' to convert non-numeric values to NaN
    numeric_series = series_a.apply(pd.to_numeric, errors='coerce')

    # apply notnull() to return a boolean series indicating which values are not null
    count = numeric_series.notnull()

    # iterates through count & check if true
    for i in range(len(count)):
        if count[i]:
            count_policy_state_junk += 1
            junk_policy_state.append(i)
        else:
            count_policy_state_clean += 1
            clean_policy_state.append(i)

    main.junk_initial.update(junk_policy_state)
    main.clean_initial.update(clean_policy_state)

    print(count_policy_state_junk)
    print(junk_policy_state)
    print(main.junk_initial)

    print(count_policy_state_clean)
    print(clean_policy_state)
    print(main.clean_initial)

    return policy_state
