import requests
from datetime import datetime
import smtplib
import time

my_email = "arrow9129402fahad@gmail.com"
password = "ookcpkhuiwglgxup"

MY_LAT = 13.097370
MY_LANG = 80.186573

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_longitude = float(data['iss_position']['longitude'])
iss_latitude = float(data['iss_position']['latitude'])

parameters = {
    'lat': MY_LAT,
    'lng': MY_LANG,
    'formatted': 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

sunrise_hour = int(sunrise) + 5
sunset_hour = int(sunset) + 5

time_now = datetime.now()
hour = time_now.hour

while True:
    time.sleep(60)
    if (MY_LAT - 5, MY_LANG - 5) <= (iss_latitude, iss_longitude) <= (MY_LAT + 5, MY_LANG + 5):
        if hour >= sunset_hour or hour <= sunrise_hour:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="fahadaameer@yahoo.com",
                                    msg="Subject:Look Up!\n\nGo outside and look up for satellite")
