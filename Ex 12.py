import sys



sys.exit()

### 1

import requests

request = "https://api.chucknorris.io/jokes/random"

response = requests.get(request).json()
print(response['value'])

### 2

import requests

def city_name():
    city = input("Name of the city: ")
    return city

def tempr_in_kelvin(city, API_key):
    request = "http://api.openweathermap.org/data/2.5/weather?q=" + city + f'APIID = {API_key}'
    response = requests.get(request).json()
    kelvin = response['main']['temperature']
    return kelvin

def kelvin_to_celsius(kelvin):
    return kelvin + 273.15

city = city_name()
API_key = input("Enter the API key: ")
celsius = kelvin_to_celsius(tempr_in_kelvin(city, API_key))
print(f"The temperature in {city} is {round(celsius, 2)} degrees Celsius.")
