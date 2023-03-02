import main


def indemnity_fraud():
    fraud_indemnity = []
    count = 0

    for i in range(len(main.CLAIM_INDEMNITY_EST_AMT_c)):
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'All Over':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 118258.5:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Complete Drivers Side':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 49868.75:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Complete Front End':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 73086.5:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Complete Passenger Side':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 85506.50:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Complete Rear End':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 19917.5:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Drivers Center':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 83830.5:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Driver Front Corner':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 61479.75:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Driver Rear Corner':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 46557.5:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'No Damage':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 16612.5:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Passenger Center':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 58335.5:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Passenger Front Corner':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 48570.5:
                fraud_indemnity.append(i)
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'Passenger Rear Corner':
            if main.CLAIM_INDEMNITY_EST_AMT_c[i] > 46471.5:
                fraud_indemnity.append(i)

    for i in fraud_indemnity:
        count += 1

    main.fraud_initial.update(fraud_indemnity)

    print(count)
    print(fraud_indemnity)
    print(main.fraud_initial)

    return indemnity_fraud
