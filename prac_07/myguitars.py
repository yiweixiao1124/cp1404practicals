import csv
from guitar import Guitar


def main():
    guitars = []

    in_file = open("guitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        guitars.sort()
        print(guitar)
    print()

    print("Sorted guitars:")
    for guitar in guitars:
        print(guitar)
    print()
    name = input("Enter guitar name: ")
    year = int(input("Enter guitar year: "))
    cost = float(input("Enter guitar cost: "))
    write_to_file(name,year,cost)


def write_to_file(name, year, cost):
    # out_file = open('guitars.csv', 'w')
    # for guitar in guitars:
    #     print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    # out_file.close()
    with open("guitars.csv", "a")as out_file:
        print(f"{name},{year},{cost}", file=out_file)


main()