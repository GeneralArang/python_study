num = int(input("정수를 입력하시오 : "))

for i in range(num+1):
    for j in range(1,num+1):
        if j<=i:
            print("*", end = "")
    print("\n")