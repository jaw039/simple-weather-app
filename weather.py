import requests
from datetime import datetime

while True:
    ## get the city name from the enduser
    city = input("Which city's weather would you like to check? \n")

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e1a450dc406ef1755ab4b44535e5de34")
    # print(response.status_code)
    # print(response.text)
    if response.status_code == 200:
        break
    else:
        print("Invalid City Name, Please Enter Again")


## stores the data into a dict
API_Date = response.json()
# print(API_Date)
# print("City name from API:", API_Date["name"])
## gets the city weather condition
weather_condition = (API_Date["weather"][0]["main"])

## get the weather temp (fahrenheit)
class KelvinToCelciusConverter:
    def convert(self, kelvin):
        return round((kelvin - 273.15) * 9 / 5 + 32)

converter = KelvinToCelciusConverter()
kelvin_value = (API_Date["main"]["temp"]) 
weather_temp = str(converter.convert(kelvin_value))

## if there is rain prints the rain status, else print no rain
if "rain" in API_Date and "1h" in API_Date["rain"]:
    print(" rain " + API_Date["rain"]["1h"])
else:
    print("No Rain Currently")

## sunrise and sunset time
sun_rise_timestamp = datetime.fromtimestamp(API_Date["sys"]["sunrise"])
weather_sunrise = sun_rise_timestamp.strftime("%I:%M %p")
sun_set_timestamp = datetime.fromtimestamp(API_Date["sys"]["sunset"])
weather_sunset = sun_set_timestamp.strftime("%I:%M %p")

print("The weather in " + city + " is " + weather_condition + " with a temperature of " + weather_temp
      + "°F.")
print("Sunrise is at " + weather_sunrise + "\nSunset is at " + weather_sunset)



# Input validation loop - If a city isn't found, ask the user to try again instead of crashing