import sys


sys.exit()

###1
class Elevator:

    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

    def go_to_floor(self, floor):
        if floor == self.current_floor:
            print(f"Press the next floor button.")

        while floor != self.current_floor:
            if floor > self.current_floor:
                self.floor_up()
                print(f"Moving up! Floor {self.current_floor}.")

            if floor < self.current_floor:
                self.floor_down()
                print(f"Moving down! Floor {self.current_floor}.")
        print(f"You're now on the floor {self.current_floor}.")

# main program

h = Elevator(10, 0)

h.go_to_floor(7)
print()
h.go_to_floor(3)
print()
h.go_to_floor(3)

### 2
class Elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

    def go_to_floor(self, floor):
        if floor == self.current_floor:
            print(f"Press the next floor button.")

        while floor != self.current_floor:
            if floor > self.current_floor:
                self.floor_up()
                print(f"Moving up! Floor {self.current_floor}.")

            if floor < self.current_floor:
                self.floor_down()
                print(f"Moving down! Floor {self.current_floor}.")
        print(f"You're now on the floor {self.current_floor}.")


class Building:
    elevators_list = []

    def __init__(self, top_floor, bottom_floor, total_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor
        self.total_elevator = total_elevators

        for e in range(total_elevators):
            self.elevators_list.append(Elevator(top_floor, bottom_floor))

    def run_elevator(self, elevator_no, destination_floor):
        if elevator_no <= 0:
            elevator_no = 1
        if elevator_no > self.total_elevator:
            elevator_no = self.total_elevator

        elevator_chosen = self.elevators_list[elevator_no-1]
        elevator_chosen.go_to_floor(destination_floor)

        print(f"Elevator {elevator_chosen} is in operation.")

###3
    def fire_alarm(self):
        for e in self.elevators_list:
            print(f"Elevator {e}:")
            e.go_to_floor(self.bottom_floor)

# main program of 2 and 3
building_A = Building(10, -2, 3)
building_B = Building(8, 0, 5)

building_A.run_elevator(2, 4)
print()
building_A.run_elevator(2, 7)
print()
print("******************************** Next Building ***************************************")
print()
building_B.run_elevator(3, 8)
print()
building_B.run_elevator(5, 6)

print()
print("######################################################################################")
print()
building_B.fire_alarm()

####### 4
from tabulate import tabulate
import random

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

# main program
name = "Grand Demolition Derby"
cars_list = []
distance = 8000
no_of_cars = 10

for i in range(no_of_cars):
    registration_no = "ABC-" + str(i + 1)
    maximum_speed = random.randint(100, 200)
    new_car = Car(registration_no, maximum_speed)
    cars_list.append(new_car)

race1 = Race(name, distance, cars_list)
race1.hour_passes()