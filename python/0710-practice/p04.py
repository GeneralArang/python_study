def Check_grade(score):
    if 100 > score >= 90:
        return print("성적이 'A'입니다.")
    elif 90 > score >= 80:
        return print("성적이 'B'입니다.")
    elif 80 > score >= 70:
        return print("성적이 'C'입니다.")
    elif 70 > score >= 60:
        return print("성적이 'D'입니다.")
    elif 60 > score >= 0:
        return print("성적이 'F'입니다.")
    else:
        return print("잘못된 입력입니다.")


score = int(input("점수를 입럭하세요."))
Check_grade(score)
