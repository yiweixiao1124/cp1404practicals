MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
menu = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = float(input("Enter score: "))
            while score < MIN_SCORE or score > MAX_SCORE:
                print("Invalid score")
                score = float(input("Enter score: "))
        elif choice == 'P':
            message = get_score_result(score)
            print(message)
        elif choice == 'S':
            print_stars(score)
        else:
            print("Invalid choice")
        print()
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


def print_stars(score):
    print('*' * int(score))


main()
