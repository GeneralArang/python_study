message = "화씨 %d도는 섭씨 %d도 입니다."
tempF = int(input("화씨"))
tempC = (tempF-32)*5/9
print(message %(tempF, tempC))
print(type(tempC))