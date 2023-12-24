from guitar import Guitar
from guitar_test import Guitar


def main():
    guitars = []

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
        guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added")
        name = input("Name: ")

        guitar_add = Guitar(name, year, cost)
        guitars.append(guitar_add)
        print(f"{guitar_add} added")


    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))

    if guitars:
        guitars.sort()
        print("These are my guitars:")

        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

    else:
        print("No guitars :( quick, go and buy someone!")
main()
