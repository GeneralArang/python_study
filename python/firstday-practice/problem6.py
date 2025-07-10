message = "입력하신 음식값이 %d원이므로 사장님이 받으실 수 있는 팁을 포함한 가격은 %d원입니다."
a = int(input("음식값"))
b = a*(1+0.1)
print(message %(a,b))