import sys



sys.exit()

#1
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

# main program
car1 = Car("ABC-123", 142)

print(f"The properties of the new car are:-\n Registration number: {car1.registration_number}\n "
      f"Maximum speed: {car1.maximum_speed}\n Current Speed: {car1.current_speed}\n Travelled distance: {car1.travelled_distance} ")



#2
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
        print(f"The current speed of the car is {car1.current_speed} km/h.")

# main program
car1 = Car("ABC-123", 142)
print(f"The maximum speed of the car is {car1.maximum_speed} km/h.")

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)


#3
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
        print(f"The current speed of the car is {car1.current_speed} km/h.")

    def drive(self, no_of_hrs):
        self.travelled_distance += no_of_hrs * self.current_speed

# main program
car1 = Car("ABC-123", 142)
car1.accelerate(60)
car1.drive(1.5)

print(f"The distance travelled by the car is {car1.travelled_distance} km.")

#4
import random
from tabulate import tabulate

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change

    def drive(self, no_of_hrs):
        self.travelled_distance += no_of_hrs * self.current_speed

# main program
cars_list = []
no_of_cars = 10
drive_hrs = 1
running_km = 0
finish_line = 10000
for c in range(no_of_cars):
    registration_number = "ABC-" + str(c+1)
    maximum_speed = random.randint(100, 200)
    car = Car(registration_number, maximum_speed)
    cars_list.append(car)

while running_km < finish_line:
    for i in range(no_of_cars):
        speed_change = random.randint(-10, 15)
        cars_list[i].accelerate(speed_change)
        cars_list[i].drive(drive_hrs)
        if running_km < cars_list[i].travelled_distance:
            running_km = cars_list[i].travelled_distance

print("Welcome to the car race! Ten cars are participating in the race and here is the table that depicts the details of each cars.")

table = [["Car no.", "Reg no.", "Max Speed(km/h)", "Current Speed(km/h)", "Distance Travelled(km)"]]
for r in range(no_of_cars):
    table.append([r+1, cars_list[r].registration_number, cars_list[r].maximum_speed, cars_list[r].current_speed,
                  cars_list[r].travelled_distance])

print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))