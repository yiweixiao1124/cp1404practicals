import random
MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
menu = "\n(G)et\n(P)rint\n(S)how\n(Q)uit"


def main():
    print(menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = random.randint(MIN_SCORE, MAX_SCORE)
            print(f"Random score: {score}")
        elif choice == 'P':
            message = get_score_result(score)
            print(message)
        elif choice == 'S':
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


main()
