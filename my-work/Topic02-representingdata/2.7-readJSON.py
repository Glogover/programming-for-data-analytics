# This program reads in JSON data from a URL and outputs it as a Python dictionary.

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)
