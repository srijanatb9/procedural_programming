import sys


<<<<<<< HEAD

=======
>>>>>>> origin/master
sys.exit()


#1
import mysql.connector

def airportNameTown(icao_cd):
    sql = 'SELECT name, municipality FROM airport WHERE ident = ' + f'"{icao_cd}"' + ";"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
<<<<<<< HEAD
            print(f"Name: {result[0][0]}, Town: {result[0][1]}")
=======
            print(f"Name: {result[0][0]}, town: {result[0][1]}")
>>>>>>> origin/master
        return

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='S0prm9oD?',
         autocommit=True
         )

i_code = input("Enter the ICAO code of the airport: ").upper()
<<<<<<< HEAD
airportNameTown(i_code)
=======
airport_name_and_town(code)
>>>>>>> origin/master


#2
import mysql.connector

def airport_type(iso_countryCd):
    sql = 'SELECT name, type FROM airport WHERE iso_country = ' f'"{iso_countryCd}"' + ' ORDER BY type;'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for rows in result:
        print(f"Name: {rows[0]}, Type: {rows[1]}")
    return

connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="S0prm9oD?",
    autocommit=True
)

iso_countryCd = input("Enter the area code: ")
airport_type(iso_countryCd)


#3
import mysql.connector
from geopy import distance

def airport_coordinates(icao_cd):
<<<<<<< HEAD
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = ' + f'"{icao_cd}"' + ";"
=======
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE gps_code = ' + f'"{icao_cd}"' + ";"
>>>>>>> origin/master
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="S0prm9oD?",
    autocommit=True
)

icao_cd_first = input("Enter the ICAO Code of the first Airport: ")
icao_cd_second = input("Enter the ICAO Code of the second Airport: ")

coordinates_1 = []
coordinates_2 = []

for g in airport_coordinates(icao_cd_first)[0]:
    coordinates_1.append(float(g))

for g in airport_coordinates(icao_cd_second)[0]:
    coordinates_2.append(float(g))

coordinates_1 = tuple(coordinates_1)
coordinates_2 = tuple(coordinates_2)

print(f"The distance between {icao_cd_first} and {icao_cd_second} is {distance.distance(coordinates_1, coordinates_2)}.")









