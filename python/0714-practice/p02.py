import random
Num_list = []
for i in range(10):
    a = random.sample(range(1,100),1)[0]#sample은 항상 리스트를 반환하므로 [0]을 붙여야 한다.
    Num_list.append(a)

print(Num_list)