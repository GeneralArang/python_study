import random
a = random.randint(1,9)
b = random.randint(1,9)
c = random.randint(1,4)

match c:
    case 1:
        d = a + b
        e = int(input(("a = %d, b = %d, a+b = ? ") %(a,b)))
        if e == d:
           print("정답입니다.")
        else:
           print("오답입니다.")
    case 2:
        d = a - b
        e = int(input(("a = %d, b = %d, a+b = ? ") %(a,b)))
        if e == d:
           print("정답입니다.")
        else:
           print("오답입니다.")
    case 3:
        d = a * b
        e = int(input(("a = %d, b = %d, a+b = ? ") %(a,b)))
        if e == d:
           print("정답입니다.")
        else:
           print("오답입니다.")
    case 4:
        d = a / b
        d = round(d,2)
        e = float(input(("a = %d, b = %d, a/b = ? ") %(a,b)))
        if e == d:
           print("정답입니다.")
        else:
           print("오답입니다.")
        