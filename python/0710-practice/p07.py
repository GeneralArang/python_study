def WhatDate():
    import random

    month_pool = [1,2,3,4,5,6,7,8,9,10,11,12]
    date_pool = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    Month = random.choice(month_pool)
    Date = random.choice(date_pool)
    print(Month)
    print(Date)

    while True:
        What_month = int(input("몇월?"))
        What_date = int(input("몇일?"))
        if What_month == Month and What_date == Date:
            print( f"\n{Month}월 {Date}일 입니다.")
            break
        else:
            print("아닙니다. 다시 입력하세요")

WhatDate()
