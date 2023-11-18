MINI_LENGTH = 8


def main():
    password = input("Enter password: ")
    check_password(password)
    the_password(password)


def check_password(password):
    while len(password) < MINI_LENGTH:
        print("The password length must be at least greater than 8 bits.")
        password = input("Enter password: ")


def the_password(password):
    print(len(password) * '*')


main()
