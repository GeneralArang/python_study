#08번

a = int(input("키를 입력하세요!"))
b = int(input("몸무게를 입력하세요"))
c = (a-100)*0.9
if c == b:
    print("표준체중")
elif c < b:
    print("과체중")
else:
    print("저체중")