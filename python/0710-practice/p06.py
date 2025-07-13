def Four_Cal(First,Second):
    import random

    First = int(input("첫번째 정수를 입력하시오"))
    Second = int(input("두번째 정수를 입력하시오"))

    cal = [1,2,3,4]

    choice_cal = random.choice(cal)

    match choice_cal:
        case 1:
            print(f"{First} + {Second} = ?")
            Answer = int(input("\n정답은 : "))
            if Answer == First + Second:
                print("\n정답입니다!!")
            else:
                print("오답입니다...")
        case 2:
            print(f"{First} - {Second} = ?")
            Answer = int(input("\n정답은 : "))
            if Answer == First - Second:
                print("\n정답입니다!!")
            else:
                print("오답입니다...")
        case 3:
            print(f"{First} * {Second} = ?")
            Answer = int(input("\n정답은 : "))
            if Answer == First * Second:
                print("\n정답입니다!!")
            else:
                print("오답입니다...")
        case 4:
            print(f"{First} / {Second} 의 몫은 ?")
            Answer = int(input("\n정답은 : "))
            if Answer == First // Second:
                print("\n정답입니다!!")
            else:
                print("오답입니다...")

First = 0
Second = 0
Four_Cal(First,Second)
