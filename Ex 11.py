import sys



sys.exit()
### 1

# Base class
class Publication:
    def __init__(self, name):
        self.name = name

# Subclass 1
class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"Book: {self.name}\nAuthor: {self.author}\nPage Count: {self.page_count}\n")

# Subclass 2
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"Magazine: {self.name}\nChief Editor: {self.chief_editor}\n")

# main program
publications = []
publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))

for p in publications:
    p.print_information()


### 2

from tabulate import tabulate
import random

# Base class
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, no_of_hrs):
        self.travelled_distance += no_of_hrs * self.current_speed

class Race:
    distance_covered = 0
    hour = 1
    index = None

    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.car_list = cars_list
        self.total_cars = len(cars_list)

    def hour_passes(self):
        while not self.race_finished():
            for i in range(self.total_cars):
                speed_change = random.randint(-10, 15)
                self.car_list[i].accelerate(speed_change)
                self.car_list[i].drive(10)
            self.print_status()

    def print_status(self):
        table = [["Car no.", "Reg no.", "Max Speed(km/h)", "Current Speed(km/h)", "Distance Travelled(km)"]]
        for i in range(no_of_cars):
            table.append(
                [i + 1, cars_list[i].registration_number, cars_list[i].maximum_speed, cars_list[i].current_speed,
                 cars_list[i].travelled_distance])

        print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

    def race_finished(self):
        for i in range(self.total_cars):
            if self.distance_covered < self.car_list[i].travelled_distance:
                self.distance_covered = self.car_list[i].travelled_distance
                index = i
                if self.distance_covered > self.distance:
                    return True

# Subclass 1
class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(registration_number, maximum_speed)

# Subclass 2
class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        self.tank_volume = tank_volume
        super().__init__(registration_number, maximum_speed)

# main program
cars_list = []
cars_list.append(ElectricCar("ABC-15", 180, 52.5))
cars_list.append(GasolineCar("ACD-123", 165, 32.3))
for c in cars_list:
    c.accelerate(random.randint(30, 60))
    c.drive(3)
    print(f"Car: {c.registration_number}\nDistance Travelled: {c.travelled_distance}\n")