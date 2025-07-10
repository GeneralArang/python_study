def calc(a,b):
    def Plus(a,b):
        return a + b
    def Minus(a,b):
        return a - b
    def multipy(a,b):
        return a * b
    def divide(a,b):
        return a / b

a = int(input("첫번째 값을 입력하시오"))
b = int(input("두번째 값을 입력하시오"))

c = Plus(a,b)
d = Minus(a,b)
e = multipy(a,b)
f = divide(a,b)
calc(a,b)
print("합 =", c," ","차 =",d, " ", "곱 =", e, " 나누기 =",f)