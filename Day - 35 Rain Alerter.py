import requests
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""  # get new api key from openweather.org

weather_params = {
    "lat": 31.520370,
    "lon": 74.358749,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}  # lat and lon of Lahore, Pakistan

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break


if will_rain:
    time.sleep(60)
    connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Don't forget your umbrella!.It is going to rain"
    )