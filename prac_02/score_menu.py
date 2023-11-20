import random
MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
menu = "(G)et\n(P)rint\n(S)how\n(Q)uit"


def main():
    print(menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = random.randint(MIN_SCORE, MAX_SCORE)
            print(f"Random score: {score}")
            random_message = get_score_result(score)
            print(random_message)
        if choice == 'P':
            message = get_score_result(score)
            print(message)
        if choice == 'S':
            for i in range(score):
                print('*', end=" ")
        else:
            print("Invalid choice")
            print(menu)
            choice = input(">>> ").upper()

    print("Goodbye")


def get_score_result(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


