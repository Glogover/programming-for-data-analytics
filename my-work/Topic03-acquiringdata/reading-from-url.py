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

