total = 0
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9

number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_items = float(input(f"Price of item{i + 1}: $"))
    total += price_of_items

if total > DISCOUNT_THRESHOLD:
    total *= DISCOUNT_RATE

print(f"Total price for 3 items is ${total:.2f}")

