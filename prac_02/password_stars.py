MINI_LENGTH = 8


def main():

    password = check_password()
    print(len(password) * '*')


def check_password():
    password = input("Enter password: ")
    while len(password) < MINI_LENGTH:
        print("Invalid passwords.")
        password = input("Enter password: ")
    return password


main()
