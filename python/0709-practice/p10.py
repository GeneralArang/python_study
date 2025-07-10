n = int(input("n을 입력하시오."))
total_sum = 0
for x in range(1,n+1):
    if x <= n:
        total_sum = total_sum + x ** 2

print("1부터 n까지 각 수의 제곱의 합은 %d입니다." %total_sum)