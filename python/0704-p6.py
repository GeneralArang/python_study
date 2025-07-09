import random
a = input("가위바위보를 입력하시오 : ")
b = random.randint(1,3)
if b==1:
    if a == "가위":
        print("비김")
    elif a == "바위":
        print("com 짐")
    else:
        print("너 이김")
elif b==2:
    if a == "바위":
        print("비김")
    elif a == "보":
        print("com 짐")
    else:
        print("너 이김")
else:
    if a == "보":
        print("비김")
    elif a == "가위":
        print("com 짐")
    else:
        print("너 이김")