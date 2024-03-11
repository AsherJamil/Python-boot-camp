import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "ff26523a15ee865d7d345192465a1be9"  # get new api key from openweather.org

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
    # Email configuration
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password
    receiver_email = "your_email@gmail.com"  # Replace with your email

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Umbrella Reminder"

    body = "Don't forget to bring an umbrella! It's going to rain in Lahore, Pakistan."

    message.attach(MIMEText(body, "plain"))

    # Connect to SMTP server and send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")
