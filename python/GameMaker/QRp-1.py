import random
import qrcode
def OX (a,b,c):
    if a == b:
        c += 1
    return c

def ROLDQR():
    OLDText = random.choice(Old_Wisdom)
    img = qrcode.make(f"<{OLDText}>")
    img.show("qrcode.png")
    Typed = input("\nQR코드로 전달된 문장을 입력하세요! : ")

Old_Wisdom = [
    "가는 말이 고와야 오는 말이 곱다",
    "호랑이도 제 말 하면 온다",
    "등잔 밑이 어둡다",
    "원숭이도 나무에서 떨어진다",
    "꿩 대신 닭",
    "세 살 버릇 여든까지 간다",
    "티끌 모아 태산",
    "백문이 불여일견",
    "웃는 얼굴에 침 못 뱉는다",
    "하늘이 무너져도 솟아날 구멍이 있다",
    "말 한마디에 천 냥 빚도 갚는다",
    "누워서 떡 먹기",
    "소 잃고 외양간 고친다",
    "돌다리도 두들겨 보고 건너라",
    "바늘 도둑이 소 도둑 된다",
    "아는 길도 물어 가라",
    "고래 싸움에 새우 등 터진다",
    "가는 날이 장날이다",
    "개구리 올챙이 적 생각 못 한다",
    "열 번 찍어 안 넘어가는 나무 없다",
    "배보다 배꼽이 크다",
    "공든 탑이 무너지랴",
    "천 리 길도 한 걸음부터",
    "빈 수레가 요란하다",
    "자라 보고 놀란 가슴 솥뚜껑 보고 놀란다",
    ]

ROLDQR()

correct = 0
while True:
    for i in range(min(len(OLDText),len(Typed))):
        OX(OLDText, Typed, correct)

    accuracy = len(OLDText) / len(Typed) * 100
    print(f"정확도는 {accuracy}%입니다.")

    Repeat = input("\n계속하시려면 ok 아니면 no를 입력하세요")
    if Repeat == "ok":
        ROLDQR()
    else:
        print("수고햇다.토닥토닥")
        break


