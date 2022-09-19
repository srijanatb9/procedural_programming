import sys



sys.exit()

#1

# december= 1st month of winter
# dec, jan, feb = winter (12, 1, 2)
# march, april, may = spring (3,4,5)
# jun, july, august = summer (6,7,8)
# sept, oct, nov = autumn (9,10,11)

seasons = ("winter", "spring", "summer", "autumn")

month = input("Enter the no. of a month (1-12): ")
if month in ('12', '1', '2'):
    s = seasons[0]
elif month in ('3', '4', '5'):
    s = seasons[1]
elif month in ('6', '7', '8'):
    s = seasons[2]
else:
    s = seasons[3]

print(f"The season in month no. {month} is {s}.")


#2

print("Enter an empty string if you want to quit.")
x = 1
names = set()

while x > 0:
    n = input("Enter a name:")
    if n != "":
        if n not in names:
            print("New name")
        if n in names:
            print("Existing name")
        names.add(n)
    else:
        break

print("The names are: ")
for n in names:
    print(n)


#3

airport = {"VNKT": "Kathmandu-International",
           "OTHH": "Qatar-International",
           "EFHK": "Helsinki-Vanta",
           "VNPL": "Solukhumbu-Phaplu",
           "VNPK": "Pokhara-International"}

print("Press A: To proceed to a new airport\n"
      "Press B: To find the information of the existing airport\n"
      "Press C: To quit.")

a = 0
while a < 1:
    print()
    opt = input("Choose one from the above options: ").upper()
    if opt == 'C':
        print("You chose to quit.")
        break
    elif opt == 'A':
        code = input("Enter the ICAO code: ").upper()
        ap = input("Enter the name of the airport: ").capitalize()
        print("You can select new options until you choose to quit.")
    elif opt == 'B':
        i_code = input("Enter the ICAO code: ").upper()
        print(f'This is {airport[i_code]} airport.')
        print("You can select new options until you choose to quit.")
    else:
        continue