"""
a = int(input("6자리 수를 입력하시오 : "))
b = a//1000
c = a%1000
print(b,",",c)
"""

num = int(input("숫자를 입력하시오 : "))
if num>=100000 and num<1000000:
    moreT=num//1000
    lessT=num%1000
    print(moreT,",",lessT)
    print(moreT+lessT)
    print(str(moreT)+","+str(lessT))
    print("%d,%d"%(moreT,lessT))
    print(f"{moreT},{lessT}")
