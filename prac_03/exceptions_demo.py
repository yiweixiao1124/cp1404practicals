"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If user input a float or a character, a Valueerror will occur.
2. When will a ZeroDivisionError occur?
This error occurs when the denominator entered by the user is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Use a while loop to check denominator. If denominator is 0, let the user reenter the denominator until it is not 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
