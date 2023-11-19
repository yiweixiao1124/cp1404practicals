"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MIN_SALES = 0
MAX_SALES = 1000
MIN_DISCOUNT = 0.1
MAX_DISCOUNT = 0.15

sales = float(input("Enter sales: $"))
while sales >= MIN_SALES:
    if sales < MAX_SALES:
        bonus = MIN_DISCOUNT
    else:
        bonus = MAX_DISCOUNT
    print("bonus = $", int(sales * bonus), sep="")
    sales = float(input("Enter sales: $"))

