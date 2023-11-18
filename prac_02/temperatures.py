def main():
    choice = input("(C)elsius or (F)ahrenheit or (Q)uit? ").upper()
    while choice != 'Q':
        while choice == 'C':
            celsius = float(input("Enter celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}℃ is equal to {fahrenheit}℉")
            choice = input("(C)elsius or (F)ahrenheit or (Q)uit? ").upper()
        while choice == 'F':
            fahrenheit = float(input("Enter fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}℉ is equal to {celsius}℃")
            choice = input("(C)elsius or (F)ahrenheit or (Q)uit? ").upper()


def celsius_to_fahrenheit(celsius):
    return 32 + celsius * 1.8


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8


main()