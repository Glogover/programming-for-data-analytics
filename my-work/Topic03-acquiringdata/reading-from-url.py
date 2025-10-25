# A program to demonstrate getting data from the web using the requests object
# Author: Marcin Kaminski

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

