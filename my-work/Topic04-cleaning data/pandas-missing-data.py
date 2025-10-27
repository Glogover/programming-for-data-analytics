# pandas-missing-data.py
# Author: Marcin Kaminski

import pandas as pd

# datadir = "../../data/"
filename = "people-100-dirty.csv"

df = pd.read_csv(filename)

# Detect missing values
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace = True)

