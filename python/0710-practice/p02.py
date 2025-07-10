def Plus(a,b):
    sum = a + b
    return sum

def Minus(a,b):
    substract = a - b
    return substract

def multipy(a,b):
    product = a * b
    return product

def divide(a,b):
    division = a / b
    return division

a = int(input("첫번째 값을 입력하시오"))
b = int(input("두번째 값을 입력하시오"))
c = Plus(a,b)
d = Minus(a,b)
e = multipy(a,b)
f = divide(a,b)
print("합 =", c," ","차 =",d, " ", "곱 =", e, " 나누기 =",f)