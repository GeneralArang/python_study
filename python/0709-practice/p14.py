maxNum = 20
number = 2
count = 0

while number < maxNum:
    divisor = 2
    prime = True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1
    if prime:
        count += 1
        print(number, end = " ")
    number += 1
