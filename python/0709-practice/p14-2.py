maxNum = 20
number = 2
count = 0

for i in range(2,maxNum+1):
    divisor = 2
    prime = True

    for divisor in range(2,number):
        if number % divisor == 0:
            prime = False
            break
    if prime:
        count +=1
        print(number,end=" ")
    number += 1