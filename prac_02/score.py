MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    score = float(input("请输入分数: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("无效的分数")
        score = float(input("请输入分数: "))
    message = get_score_result(score)
    print(message)


def get_score_result(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()