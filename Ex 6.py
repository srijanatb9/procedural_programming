import sys



sys.exit()

#1
from random import randint
def dice_roll():
    return randint(1,6)

t = 0
roll = None

while roll != 6:
    roll = dice_roll()
    t += 1
    print(f'For try number {t}, the output is {roll}.')
print(f'It took {t} to get 6.')


#2
def dice_roll(side):
    return randint(1, side)

side = int(input("Enter your desired maximum no. on the dice: "))
t = 0
roll = None

while roll != side:
    roll = dice_roll(side)
    t += 1
    print(f'For try number {t}, the output is {roll}.')
print(f'It took {t} tries to get desired max no. {side} on the dice.')

#3

def gasoline(g):
    return g * 3.785

print("Enter a negative value to stop the program.")
l = 1

while l > 0:
    g = float(input("Enter the quantity of gasoline in gallons: "))
    if g < 0:
        break
    else:
        l = gasoline(g)
    print(f'{g} American gallons is equal to {l} litres.')

#4

def numList (numl):
    add = 0
    for n in numl:
        add = add + n
    return add

num_l = [-2, -1, 0, 3, 5, 7]
print(numList(num_l))


#5

def numList (numl):
    newnl = []

    for n in numl:
        if n % 2 == 0:
            newnl.append(n)
        else:
            continue
    return newnl

num_l = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10]

print(f"The original list of integers: {num_l}")
print(f"The list after excluding uneven numbers: {numList(num_l)}")

#6
import math

def pizza(d, p):
    up = 1/4*(math.pi*(d/100)**2)/p
    return up

print("For pizza no. 1")
dm = int(input("Enter the diameter in cm: "))
pr = int(input("Enter the price: "))

print("For pizza no. 2")
dm2 = int(input("Enter the diameter in cm: "))
pr2 = int(input("Enter the price: "))

piz = pizza(dm, pr)
piz2 = pizza(dm2, pr2)
print(f'The unit prices (i.e price per square meter) of pizza no.1 and pizza no.2 are {piz} euros and {piz2} euros respectively.')

if piz < piz2:
    print(f"Pizza no.1 provides better value for money.")
else:
    print(f"Pizza no.2 provides better value for money.")