x = int(input("약수를 알고싶은 정수를 입력하시오"))
y = 0
for y in range(1,x+1):
    if x%y == 0:
        print(y, end = " ")