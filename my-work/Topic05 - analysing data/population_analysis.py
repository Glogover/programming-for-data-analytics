# Analysing population wrong
# Author: Marcin Kaminski

import pandas as pd

FILENAME = "population_for_analysis.csv" 

df = pd.read_csv(FILENAME)

print(df.head(3))
headers = df.columns[1:]
print(headers)
district = headers[0]
print(df[district].describe())
print(df[district])


