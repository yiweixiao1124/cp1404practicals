import csv
from guitar import Guitar


def main():
    guitars = []

    in_file = open("guitars.csv", 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)
    print()
    guitars.sort()
    print("Sorted guitars:")
    for guitar in guitars:
        print(guitar)
    print()
    name = input("Enter guitar name: ")
    while name != "":
        year = int(input("Enter guitar year: "))
        cost = float(input("Enter guitar cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Enter guitar name: ")

    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


main()
