# This program reads in JSON data from a URL.

import json
import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=2))

