import main


def vehicle_year():  # done
    junk_vehicle_year = []
    clean_vehicle_year = []

    count_vehicle_year_junk = 0
    count_vehicle_year_clean = 0

    # counts how many entries of one are greater than two
    for col in range(len(main.CLMT_VEH_YR)):
        if main.CLMT_VEH_YR[col] == 1900:
            count_vehicle_year_junk += 1
            junk_vehicle_year.append(col)
        else:
            count_vehicle_year_clean += 1
            clean_vehicle_year.append(col)

    main.junk_initial.update(junk_vehicle_year)
    main.clean_initial.update(clean_vehicle_year)

    print(count_vehicle_year_junk)
    print(junk_vehicle_year)
    print(main.junk_initial)

    print(count_vehicle_year_clean)
    print(clean_vehicle_year)
    print(main.clean_initial)

    return vehicle_year
