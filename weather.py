import requests

city = input("Which city's weather would you like to check? \n")

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=city&appid=e1a450dc406ef1755ab4b44535e5de34")
print(response.status_code)
# print(response.text)

API_Date = response.json()
# print(API_Date)

print(API_Date["weather"][0]["main"])
print(API_Date["main"]["temp"])
print(API_Date['rain']["1h"])

