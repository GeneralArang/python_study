x = int(input("정수를 입력하시오."))
for a in range(1,x+1):
    if x % a == 0:
        print(a, end=" ")