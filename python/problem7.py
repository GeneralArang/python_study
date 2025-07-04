x1 = int(input("첫번째점 x좌표"))
y1 = int(input("첫번째점 y좌표"))
x2 = int(input("두번쨰점 x좌표"))
y2 = int(input("두번째점 y좌표"))

from math import*
distance = sqrt((x2-x1)**2+(y2-y1)**2)

print("두 점사이의 거리는 %d입니다." %distance)