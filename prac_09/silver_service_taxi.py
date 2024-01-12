# silver_service_taxi.py
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odo}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f} plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + SilverServiceTaxi.flagfall