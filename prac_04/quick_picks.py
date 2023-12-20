import random
NUMBERS_OF_LINES = 6
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 45
number_of_picks = int(input("How many quick picks: "))
while number_of_picks <= 0:
    print("Invalid number")
    number_of_picks = int(input("How many quick picks: "))

for i in range(number_of_picks):
    quick_picks = []
    for j in range(NUMBERS_OF_LINES):
        number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        while number in quick_picks:
            number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        quick_picks.append(number)
    quick_picks.sort()
    print(" ".join(f"{number:2}".format(number) for number in quick_picks))
