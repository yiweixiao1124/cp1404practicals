"""
Word Occurrences
Estimate: 20 minutes
Actual:  30  minutes
"""
def main():
    email_and_name = {}
    SPECIAL_CHARACTER = "@"

    email = input("Email (contain@): ")
    while email != "":
        while SPECIAL_CHARACTER not in email:
            print("error")
            email = input("Email (contain@): ")
        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation != 'y' and confirmation != "":
            name = input("Name: ")
        email_and_name[email] = name
        email = input("Email (contain@): ")
    print_email(email_and_name)


def print_email(email_and_name):
    for email, name in email_and_name.items():
        print(f"{name} ({email})")


def get_name(email):
    prefix = email.split("@")[0]
    first_names = prefix.split('.')
    name = ' '.join(first_names).title()
    return name


main()