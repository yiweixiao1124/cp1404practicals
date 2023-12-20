MENU = "(C)elsius or (F)ahrenheit or (Q)uit? "


def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'F':
            fahrenheit = celsius_to_fahrenheit()
        elif choice == 'C':
            celsius = fahrenheit_to_celsius()
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>>").upper()
    print("Goodbye.")


def celsius_to_fahrenheit(celsius):
    celsius = float(input("Enter celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result is: {fahrenheit:.2f}℉")
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    fahrenheit = float(input("Enter fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result is: {celsius:.2f}℃")
    return celsius


main()