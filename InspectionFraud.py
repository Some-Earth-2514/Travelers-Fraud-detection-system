import main


def inspection_fraud():
    fraud_inspections = []
    count_inspections = 0

    for i in range(len(main.APPR_DAM_EST_REC_CNT_c)):
        if main.APPR_DAM_EST_REC_CNT_c[i] >= 4:
            fraud_inspections.append(i)
            count_inspections += 1

    main.fraud_initial.update(fraud_inspections)

    print(count_inspections)
    print(fraud_inspections)
    print(main.fraud_initial)
