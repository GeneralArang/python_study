#10번

x = float(input("x값을 입력하시오."))
if x <= 0:
    a = x**2 - 9*x + 2
else:
    a = 7*x + 2
print("f(%d)의 함수값은 %d입니다."%(x,a))