import sys


sys.exit()

#1
length = int(input("Enter the length of a zander:"))
size = 42 - length
if length != 42 and length < 42:
    print(f"Release the fish back into the pond because the size of the caught fish is {size} cm below the size limit.")
else:
    print(f"Whoa! You have caught a zander.")


#2
cabin = input("Enter the cabin class:")
if cabin == 'LUX':
    print("upper-deck cabin with a balcony")
elif cabin == 'A':
    print("above the car deck, equipped with a window.")
elif cabin == 'B':
    print("windowless cabin above the car deck.")
elif cabin == 'C':
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


#3
bio_gen = input("Enter your biological gender:")
hemo_v = int(input("Enter your hemoglobin value:"))
if bio_gen == "female" and 117<hemo_v<155:
    print("The hemoglobin value is normal.")
elif bio_gen == "female" and hemo_v<=117:
    print("The hemoglobin value is low.")
elif bio_gen == "female" and hemo_v>=155:
    print("The hemoglobin value is high.")
elif bio_gen == "male"and 134<hemo_v<167:
    print("The hemoglobin value is normal.")
elif bio_gen == "male" and hemo_v <= 134:
    print("The hemoglobin value is low.")
elif bio_gen == "male" and hemo_v >= 167:
    print("The hemoglobin value is high.")
else:
    print("")


#4
year = int(input("Enter a year:"))
if year%4==0:
    print("It's a leap year.")
elif year%100==0 and year%400==0:
    print("It's a leap year.")
else:
    print("Sorry! It's not a leap year.")

