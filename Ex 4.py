import sys


sys.exit()

#1
num = 1

while num < 1000:
    num += 1

    if num % 3 == 0:
        print(num)


#2
x = 1

while x > 0:
    inch = int(input("Enter the length in inches: "))

    if inch < 0:
        break
    else:
        cm = inch * 2.54
        print(f'{inch} inches is {cm} cms.')


#3
print("Enter an empty string if you want to quit.")
x = 1
num_l = []

while x > 0:
    num = input("Enter a number: ")

    if num == "":
        break
    else:
        num_l.append(num)

largest = max(num_l)
smallest = min(num_l)
# print(num_l)
print(f'The largest and the smallest numbers received are {largest} and {smallest} respectively.')


#4
import random

print("It's a game! The computer draws random numbers from 1 to 10, and you've to guess it.")
x = 0
rand_num = random.randint(0, 10)

while x < 1:
    guessN = int(input("Here you go, guess the number: "))
    print(rand_num)

    if rand_num == guessN:
        print("Correct")
        break
    elif rand_num < guessN:
        print("Too high")
    else:
        print("Too low")


#5
t = 1
while t <= 5:
    userN = input("Enter your username: ")
    passW = input("Enter your password: ")
    t += 1
    if userN != 'python' and passW != 'rules':
        print("Enter again!")
        continue
    else:
        print("Welcome")
        break
else:
    print("Access denied.")


#6
import random

#N = The total no. of random points
#n = The no. of points that fall inside the circle
N = int(input("Enter the no. of points to be generated: "))
n = 0
x = 0

while x < N:
    x += 1
    pX = random.uniform(-1, 1)
    pY = random.uniform(-1, 1)
    if pX ** 2 + pY ** 2 < 1:
        n += 1

piApprox = (4 * n)/N
print(f"The approximate value of pi is {piApprox}.")
