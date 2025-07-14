total_sum = 0
a = list()
print("값들을 입력하고 끝내려면 end를 입력하시오")
for i in range(0,1000):
    val = input("값을 입력하시오")
    if val == "end":
        break
    a.append(int(val)) #이런 방식으로 쓰면 비어있는 리스트에 for구문이 돌때마다 차례대로 리스트값으로 추가된다. 인풋을 int로 받으면 숫자가 되기때문에 문자를 쓰고 싶으면 나중에 값을 인트로 바꿔야한다.

for j in range(0,i):
    total_sum = total_sum + a[j]

print(a)
print(total_sum)