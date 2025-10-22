import urllib.request
import json

with urllib.request.urlopen('https://api.agify.io/?name=Kamil') as response:
	data = json.load(response)

print(data)
print(f"Imię: {data['name']}, Przewidywany wiek: {data['age']}, Liczba próbek: {data['count']}")
