a_list1 = []
for i in range(1000):
    val = input("값을 입력하시오")
    if val == "end":
        break
    a_list1.append(int(val))
print(a_list1)
a_set = set(a_list1)
a_list2 = list(a_set)
a_list2.sort()
print(a_list2)
