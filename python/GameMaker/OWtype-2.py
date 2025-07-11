def OX (a,b,c):
    if a == b:
        c += 1
    return c

import random

Old_Wisdom2 = [
("가는 말이 고와야", "오는 말이 곱다"),
("호랑이도 제 말", "하면 온다"),
("등잔 밑이", "어둡다"),
("원숭이도 나무에서", "떨어진다"),
("세 살 버릇", "여든까지 간다"),
("티끌 모아", "태산"),
("백문이", "불여일견"),
("웃는 얼굴에", "침 못 뱉는다"),
("하늘이 무너져도", "솟아날 구멍이 있다"),
("말 한마디에", "천 냥 빚도 갚는다"),
("누워서", "떡 먹기"),
("소 잃고", "외양간 고친다"),
("돌다리도 두들겨 보고", "건너라"),
("바늘 도둑이", "소 도둑 된다"),
("아는 길도", "물어 가라"),
("고래 싸움에", "새우 등 터진다"),
("가는 날이", "장날이다"),
("개구리 올챙이 적", "생각 못 한다"),
("열 번 찍어", "안 넘어가는 나무 없다"),
("배보다", "배꼽이 크다"),
("공든 탑이", "무너지랴"),
("천 리 길도", "한 걸음부터"),
("빈 수레가", "요란하다"),
("자라 보고 놀란 가슴", "솥뚜껑 보고 놀란다"),
]

front, back = random.choice(Old_Wisdom2)

print(f"속담 : \"{front}__________\"")
print("5번의 기회가 주어집니다.")
answer = input("뒷부분을 입력하세요 : ").strip()

j=0
correct = 0
for j in range(1,6):
    for i in range(min(len(back),len(answer))):
        OX(back,answer,correct)
    
    accuracy = len(answer) / len(back) * 100

    if back == answer:
        print("\n정확도",accuracy,"%")
        print("정답입니다.참 잘했어요!!")
        break
    else:
        hint1 = back[0]
        hint2 = back[1]
        length = len(back)
        print(f"오답입니다. 힌트는 {hint1}{hint2}이고 길이는 {length}입니다.")
        answer = input("다시! : ").strip()

if accuracy != 100:
    print("\n실패했습니다. 연습하세요!!")