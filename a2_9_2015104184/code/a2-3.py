import requests
import json

apikey = "2b12ec57f25abbcddb1c965021d4b19d"
cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

api="https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
k2c = lambda k: k-273.15

for name in cities:
    url = api.format(city=name, key=apikey)
    r = requests.get(url)
    data = json.loads(r.text)

    print("+ CITY =", data["name"])
    print("| WEATHER =", data["weather"][0]["description"])
    print("| MIN TEMP =", k2c(data["main"]["temp_min"]))
    print("| MAX TEMP =", k2c(data["main"]["temp_max"]))
    print("| HUMIDITY =", k2c(data["main"]["humidity"]))
    print("| PRESSURE =", k2c(data["main"]["pressure"]))
    print("| DEG =", k2c(data["wind"]["deg"]))
    print("| SPEED =", k2c(data["wind"]["speed"]))
    print()