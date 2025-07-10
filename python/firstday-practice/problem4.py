message = "%s시간 %s분은 %s초입니다."
a = int(input("시간"))
b = int(input("분"))
c = (a*60*60) + (b*60)
print(message %(a,b,c))