import math
import sys


sys.exit()

#1
name = input("Enter your name:")
print(f'Hello, {name}!')


#2
p = math.pi

r = float(input("Enter the radius: "))
area = p*r*r

print(f'The area of the circle is {area}.')

#3
l = float(input("Enter the length of a rectangle: "))
b = float(input("Enter the breadth of a rectangle: "))

p = 2*(l+b)
a = l*b

print(f'The perimeter and area of a rectangle are {p} and {a} respectively.')

#4
first = int(input("Enter an interger: "))
second = int(input("Enter an interger: "))
third = int(input("Enter an interger: "))

sum = first + second + third
product = first * second * third
avg = sum/3

print(f'The sum, product, and average of the numbers are {sum}, {product}, and {avg} respectively.')

#5
t = float(input("Enter talents:\n"))
p = float(input("Enter pounds:\n"))
l = float(input("Enter lots:\n"))

w = l*13.3 + p*32*13.3 + t*20*32*13.3
kg = int(w/1000)
g = round(w%1000, 2)

print(f'The weight in modern units:\n {kg} kilograms and {g} grams.')


#6
from random import randint
three_digit_code = ''
for a in range(3):
    three_digit_code = three_digit_code + str(randint(0, 9))
print(f'The three digit code: {three_digit_code}.')

four_digit_code = ''
for a in range(4):
    four_digit_code = four_digit_code + str(randint(1, 6))
print(f'The four digit code: {four_digit_code}.')






