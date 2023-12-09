"""
Word Occurrences
Estimate: 20 minutes
Actual:  30  minutes
"""
email_and_name = {}

email = input("Email: ")
while email != "":
    name = email.split('@')[0]
    first_names = name.split('.')
    first_names = [part.title() for part in first_names]
    name = ' '.join(first_names)
    if email not in email_and_name:
        choice = input(f"Is your name {name}? (Y/n) ").lower()
        if choice != 'y':
            name = input("Name: ")
    email_and_name[email] = name

    email = input("Email: ")

for email, name in email_and_name.items():
    print(f"{name} ({email})")