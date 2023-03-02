import main


def alea_fraud():
    fraud_ALAE = []
    count_ALAE = 0
    total_legal_fees = 0

    for i in range(len(main.CLAIM_EXPENSE_EST_AMT_c)):
        # check bodily & multiple
        # if VEH_PRIMARY_PT_OF_DAMAGE is not none and AUTO_ACCIDENT_DESC is multi
        # multi by collision cost
        total_legal_fees = main.BI_CLMT_CNT_c[i] * 15785
        if main.VEH_PRIMARY_PT_OF_DAMAGE_c[i] == 'No Damage':
            total_legal_fees += 0
        else:
            total_legal_fees += 4698
        if main.CLAIM_EXPENSE_EST_AMT_c[i] > total_legal_fees:
            fraud_ALAE.append(i)
            count_ALAE += 1

    main.fraud_initial.update(fraud_ALAE)

    print(count_ALAE)
    print(fraud_ALAE)
    print(main.fraud_initial)

    return alea_fraud
