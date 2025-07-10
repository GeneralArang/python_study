import random
import time
sentences = [
    "밥은 먹고 다니냐?", 
    "느그 아부지 뭐 하시노?",
    "형이... 왜 거기서 나와?",
    "내가... 웃는 게 웃는 게 아니야.",
    "묻고 더블로 가!",
    "어이가 없네?",
    "지금... 장난하나?",
    "계란이 왔어요~",
    "그거 아냐? 나 지금 되게 신나!",
    "진짜 X같네 진짜!",
    "May the Force be with you.",
    "I'm going to make him an offer he can't refuse.",
    "Here's looking at you, kid.",
    "You talking to me?",
    "Life is like a box of chocolates. You never know what you're gonna get.",
    "I'll be back.",
    "Why so serious?",
    "To infinity and beyond!",
    "I see dead people.",
    "My precious."]

target = random.choice(sentences)
print("\n다음 문장을 그대로 입력하세요:\n")
print(f"{target}\n")

input("준비가 되면 Enter를 누르세요!")

start_time = time.time()

typed = input("\n입력 : ")

end_time = time.time()
elapsed = end_time - start_time

correct = 0
for i in range(min(len(target), len(typed))): #len -> 길이를 구하는 함수
    if target[i] == typed[i]:
        correct += 1

accuracy = correct / len(target) * 100 # 짧게 타이핑을 했을 경우에 정확도가 원래 문장 길이를 기준으로 하므로 위에서 최소값을 기준으로 for구문을 돌린다.
speed = len(typed) / elapsed * 60

print("\n결과")
print(f"걸린 시간 : {elapsed:.2f}초")
print(f"정확도: {accuracy : .2f}%")
print(f"타자속도 : {speed:.2f}자/분")
