# Program showing how to read JSON from a url using Pandas
# Author: Marcin Kaminski

import pandas as pd
import json

# this one does not work easily

url = "https://api.open-meteo.com/v1/forecast?latitude=52.8436&longitude=-8.9864&daily=temperature_2m_max,temperature_2m_min"

df = pd.read_json(url)

print(df.head(3))

