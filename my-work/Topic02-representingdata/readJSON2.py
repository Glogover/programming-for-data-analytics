# This program reads in JSON data from a URL and prints out all bank holidays in England and Wales.

import json
import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

for event in data['england-and-wales']['events']:
    print(f"{event["date"]}: {event["title"]}")

