# Program that reads in the meteo data correctly
# Author: Marcin Kaminski

import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=52.8436&longitude=-8.9864&daily=temperature_2m_max,temperature_2m_min&format=csv"


df = pd.read_csv(url, header = 2 )
print(df.head(3))
print(df.info())

