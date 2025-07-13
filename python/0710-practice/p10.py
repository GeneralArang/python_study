def testPrime(End_number):
    print("\n마지막 숫자를 입력하면 1에서 입력한 마지막 숫자까지의 소수를 구하는 프로그램입니다.")
    End_number = int(input("\n마지막 숫자를 입력하시오 : "))



    for i in range(1,End_number):
        count = 0
        for j in range(1,i):
            if i % j == 0:
                count += 1

        if count == 1:
            print(f"{i}", end= " ")

n = 0
testPrime(n)