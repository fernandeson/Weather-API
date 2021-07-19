import requests

# ------------- CONSTANTS ------------- #
URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "ed8c843add1241534d0b15b7e47d1ea5"
MY_LAT = -18.923250
MY_LON = -48.273739
LANGUAGE = "pt_br"
UNITS = "metric"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "lang": LANGUAGE,
    "units": UNITS
}

response = requests.get(url=URL, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = [weather_data["hourly"][i] for i in range(12)]

for i in range(12):
    if weather_slice[i]["weather"][0]["id"] <= 700:
        print("Bring an umbrella")
        break

