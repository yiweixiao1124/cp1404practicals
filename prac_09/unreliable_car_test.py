from unreliable_car import UnreliableCar


def main():
    my_unreliable_car = UnreliableCar("Old Clunker", 100, 50)

    distance_driven = my_unreliable_car.drive(100)
    print(f"Attempted to drive 100km but only drove {distance_driven}km")
    print(my_unreliable_car)


main()
