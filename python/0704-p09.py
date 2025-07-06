import random
a = random.randint(-99,99)
b = random.randint(-99,99)
c = random.randint(1,4)
if c == 1:
    d = a + b
    e = int(input(("a = %d, b = %d, a+b = ? ") %(a,b)))
    if e == d:
        print("정답입니다.")
    else:
        print("오답입니다.")
elif c == 2:
    d = a - b
    e = int(input(("a = %d, b = %d, a-b = ? ") %(a,b)))
    if e == d:
        print("정답입니다.")
    else:
        print("오답입니다.")
elif c == 3:
    d = a * b
    e = int(input(("a = %d, b = %d, a*b = ? ") %(a,b)))
    if e == d:
        print("정답입니다.")
    else:
        print("오답입니다.")
elif c == 4:
    d = a // b
    e = int(input(("a = %d, b = %d, a/b = ? ") %(a,b)))
    if e == d:
        print("정답입니다.")
    else:
        print("오답입니다.")