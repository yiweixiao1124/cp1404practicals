"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Numbers and denominators are not valid.
2. When will a ZeroDivisionError occur?
Denominators are 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Use a while loop to check denominator. If denominator is 0, let the user reenter the denominator until it is not 0.
"""
valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("Cannot divide by zero!")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero")
print("Finished.")
