import random

MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    score = get_score()
    grade = get_grade(score)
    print(grade)
    random_score = random.uniform(MIN_SCORE, MAX_SCORE)
    print(f"Random score: {random_score}")
    random_grade = get_grade(random_score)
    print(random_grade)


def get_grade(score):
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Passable"
    else:
        message = "Bad"
    return message


def get_score():
    score = float(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

main()
