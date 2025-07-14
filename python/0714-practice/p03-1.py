key1 = [1,2,3,4,5,6,7,8,9]
val1 = ["가", "나", "다", "라", "마", "바", "사", "아", "자", "차"]
dic1 = zip(key1,val1)
print(dic1)
dic2 = dict(zip(key1,val1)) # zip으로 두 리스트를 묶은 후 이를 리스트로 만듬
print(dic2)