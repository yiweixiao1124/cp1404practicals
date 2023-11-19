import random
MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    score = float(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    message = get_score_result(score)
    print(message)

    random_score = random.randint(MIN_SCORE, MAX_SCORE)
    print(f"Random score: {random_score}")
    random_message = get_score_result(random_score)
    print(random_message)


def get_score_result(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()