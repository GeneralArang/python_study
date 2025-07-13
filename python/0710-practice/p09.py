def GCO():
    a = int(input("첫번째 정수를 입력하시오 : "))
    b = int(input("두번째 정수를 입력하시오 : "))
    c = min(a,b)+1

    for i in range(1,c):
        if a % i == 0 and b % i == 0:
            c = i

    print(f"두 수의 최대공약수는 {c}입니다.")

GCO()
