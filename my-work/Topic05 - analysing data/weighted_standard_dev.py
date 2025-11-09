import pandas as pd
import numpy as number_people

FILENAME = "population_for_analysis.csv"

df = pd.read_csv(FILENAME)

#print (df.head(3))
headers = df.columns[1:]
print(headers)
district = headers[0]
# this is incorrect
print(df[district].descrive())

