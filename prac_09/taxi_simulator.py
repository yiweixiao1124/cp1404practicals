from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    MENU = "q)uit, c)hoose taxi, d)rive"

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':

        if choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${total_bill:.2f}")
            else:
                print("Invalid taxi choice")
                print(f"Bill to date: ${total_bill:.2f}")
            print(MENU)
            choice = input(">>> ").lower()
        elif choice == 'd':
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
            print(f"Bill to date: ${total_bill:.2f}")
            print(MENU)
            choice = input(">>> ").lower()
        elif choice != 'q':
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").lower()

    print(f"Bill to date: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()