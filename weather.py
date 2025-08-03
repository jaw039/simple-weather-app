import requests

## get the city name from the enduser
city = input("Which city's weather would you like to check? \n")
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=city&appid=e1a450dc406ef1755ab4b44535e5de34")
# print(response.status_code)
# print(response.text)

## stores the data into a dict
API_Date = response.json()
# print(API_Date)

## gets the city weather condition
print(API_Date["weather"][0]["main"])

## get the weather temp (fahrenheit)
class KelvinToCelciusConverter:
    def convert(self, kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32

converter = KelvinToCelciusConverter()
kelvin_value = (API_Date["main"]["temp"]) 
print(converter.convert(kelvin_value))

## if there is rain prints the rain status, else print no rain
if "rain" in API_Date and "1h" in API_Date["rain"]:
    print(API_Date["rain"]["1h"])
else:
    print("No Rain Today")

