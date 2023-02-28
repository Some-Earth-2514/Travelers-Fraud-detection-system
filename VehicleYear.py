import main

junk_veh_yr = []

count = 0
# counts how many entries of one are greater than two
for col in range(len(main.CLMT_VEH_YR)):
    if main.CLMT_VEH_YR[col] == 1900:
        count += 1
        junk_veh_yr.append(col)
print(count)
print(junk_veh_yr)
