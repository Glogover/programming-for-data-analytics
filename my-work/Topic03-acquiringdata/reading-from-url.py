# A program to demonstrate getting data from the web using the requests object
# Author: Marcin Kaminski

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)
# we can now analyze the data
for event in data["northern-ireland"]["events"]:
    #print(f"{event}")
    print(f"{event['title']} on {event['date']}")

url = "https://api.open-meteo.com/v1/forecast?latitude=52.8436&longitude=-8.9864&hourly=temperature_2m&timezone=GMT"
response = requests.get(url)
print(response.text)

