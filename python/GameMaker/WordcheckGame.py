import random
import time
import math

Word = ["텀블러", "책상", "노트북", "연필", "의자", "커피잔", "핸드폰", "창문", "바람", "하늘"]
Life = 3
score = 0
duration = 2


print("게임을 시작합니다. 2초안에 단어를 입력하세요")
print("2초를 초과할때마다 생명력이 감소합니다.")

while True:
    Give = random.sample(Word,1)[0]
    print(f"주어진 단어는 <{Give}>입니다.")
    input("준비가 되면 Enter를 누르세요.")
#시간 측정
    start_time = time.time()
    Answer = input("\n 정답 : ")
    end_time = time.time()
    duration = end_time - start_time
    Life = Life - math.floor(duration)//2
#정오 판단
    if Answer == Give:
        print("정답입니다.")
        score += 1
    else:
        print("오답입니다.")
#생명력 판단
    if Life <= 0:
        print("생명력을 다하였습니다.")
        break
    if 3 >= Life > 0:
        print(f"남은 생명력은 {Life}입니다.")

    print(f"현재 점수는 {score}입니다.")
    print("\n다음 문제 입니다.")