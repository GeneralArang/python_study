r = int(input("원의 반지름을 입력하시오!"))
Area = 3.141592 * r**2
if r > 0:
    print("원의 면적은 %d입니다" %Area)
else:
    print("잘못된 값입니다.")