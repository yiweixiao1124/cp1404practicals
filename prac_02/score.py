MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

score = float(input("Enter score: "))
while score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
    score = float(input("Enter score: "))

if score >= EXCELLENT_THRESHOLD:
    message = "Excellent"
elif score >= PASS_THRESHOLD:
    message = "Passable"
else:
    message = "Bad"

print(message)
