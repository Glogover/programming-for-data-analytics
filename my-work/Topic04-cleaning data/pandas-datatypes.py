# pandas-datatypes.py
# Author: Marcin Kaminski

import pandas as pd

filename = "people-100-dirty.csv"

df = pd.read_csv(filename)

print(df.info())

df['Date of birth'] = pd.to_datetime(df['Date of birth'])
#df['nmeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')

print(df.info())

# standardise data
df['Email'] = df['Email'].str.lower().str.strip()
print(df.head(5))



