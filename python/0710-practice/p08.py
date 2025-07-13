def Number_count_Write():
    Numb = [0,1,2,3,4,5,6,7,8,9]
    Voice = ["","일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]


    Numb_Write = int(input("\n최대 천의 자리 숫자를 입력하시오 : "))

    #아래의 문제점 = 실수가 나옴 -> 나머지가 자리수가 아래가 되고 그때 가장 윗 자리 수를 남긴다.
    Thousand = Numb_Write // 1000
    Hundred = (Numb_Write % 1000) //100
    Ten = (Numb_Write % 100) // 10
    One = Numb_Write % 10
    Numb_list = [Thousand, Hundred, Ten, One]


    print(Thousand, end=" ")
    print(Hundred, end=" ")
    print(Ten, end=" ")
    print(One)


    for i in range(0,10):
        if Numb[i] == Thousand:
            break
    for j in range(0,10):
        if Numb[j] == Hundred:
            break
    for k in range(0,10):
        if Numb[k] == Ten:
            break
    for l in range(0,10):
        if Numb[l] == One:
            break

    if Thousand != 0:
        print(f"{Voice[Thousand]}천",end="")
    if Hundred != 0:
        print(f"{Voice[Hundred]}백",end="")
    if Ten != 0:
        print(f"{Voice[Ten]}십",end="")

    print(f"{Voice[One]}")

Number_count_Write()