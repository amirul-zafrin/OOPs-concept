from enum import Enum

class Rate(Enum):
    HOURLY = 1
    DAILY = 2
    WEEKLY = 3

class Rental:
    def __init__(self, n_rented, duration, hourly_rate, daily_rate, weekly_rate, available_units):
        self.n_rented = n_rented
        self.duration = duration
        self._hourly_rate = hourly_rate
        self._daily_rate = daily_rate
        self._weekly_rate = weekly_rate
        self.__available_units = available_units

    def availability(self):
        return self.available_units > self.n_rented

    def set_rate(self, rate):
        if rate == Rate.HOURLY:
            self._hourly_rate = self._hourly_rate
        if rate == Rate.DAILY:
            self._daily_rate = self._daily_rate
        if rate == Rate.WEEKLY:
            self._weekly_rate = self._weekly_rate

    def get_rate(self, rate):
        if rate == Rate.HOURLY:
            return self._hourly_rate
        if rate == Rate.DAILY:
            return self._daily_rate
        if rate == Rate.WEEKLY:
            return self._weekly_rate

    def charge(self, rate):
        if rate == Rate.HOURLY:
            return self._hourly_rate * self.duration
        if rate == Rate.DAILY:
            return self._daily_rate * self.duration
        if rate == Rate.WEEKLY:
            return self._weekly_rate * self.duration
    
    @property
    def available_units(self):
        return self.__available_units

    @available_units.setter
    def available_units(self, value):
        if value < 0:
            raise ValueError("Units must be positive")
        self.__available_units = value
    
    def __str__(self):
        return f"Store have {self.available_units} units available"

class BikeRental(Rental):
    def __init__(self, n_rented, duration, hourly_rate, daily_rate, weekly_rate, available_units, discount):
        super().__init__(n_rented, duration, hourly_rate, daily_rate, weekly_rate, available_units)
        self.__discount = discount
    
    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        if value < 0 or value > 1:
            raise ValueError("Discount must be between 0 and 1")
        self.__discount = value

    def charge(self, rate):
        return super().charge(rate) * (1 - self.__discount) if rate == Rate.WEEKLY else super().charge(rate)

    def __str__(self):
        return f"Store have {self.available_units} units of bike available"


bike = BikeRental(2, 10, 1.5, 2.5, 3.5, 10, discount=0.2)
print(f"Charge for {bike.duration} hours: RM {bike.charge(Rate.HOURLY):.2f}") # RM 15.00
print(f"Charge for {bike.duration} weeks: RM {bike.charge(Rate.WEEKLY):.2f}") # RM 28.00 after discount