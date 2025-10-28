# Author: Marcin Kaminski

import requests

url = "https://api.myip.com"
response = requests.get(url)
data = response.json()
print(data)