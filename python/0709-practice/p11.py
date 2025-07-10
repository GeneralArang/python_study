a = int(input("첫번째 정수를 입력하시오 : "))
b = int(input("두번째 정수를 입력하시오 : "))
common = 0
max = a
if a < b:
    max = b
for i in range(1,max):
    if a % i == 0 and b % i == 0:
        common = i

print(a,"와",b,"의 최대공약수는", common,"입니다.")