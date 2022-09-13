import sys


sys.exit()

#1
import random
d = int(input("Enter the no. of dice to roll: "))
sum = 0

for x in range(d):
    dice = random.randint(1,6)
    print(dice)
    sum = sum + dice

print(f'The sum of the numbers on the dice is {sum}.')


#2
print("Enter an empty string if you want to quit.")
x = 1
num_l = []

while x > 0:
    num = input("Enter a number: ")

    if num == "":
        break
    else:
        num_l.append(int(num))

num_l.sort(reverse=True)
print(num_l)
print(f"The five greatest numbers are {num_l[0:5]}.")


#3
num = int(input("Enter a number: "))

if num >= 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f'{num} is not a prime number.')
            break
    else:
        print(f'{num} is a prime number.')

else:
    print(f'{num} is neither a prime or a composite number.')


#4
city = []

for c in range(5):
    n_city = input("Enter the name of a city: ")
    city.append(n_city)
#print(city)

for c in city:
    print(c)