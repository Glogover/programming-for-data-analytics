# pandas-datatypes.py
# Author: Marcin Kaminski

import pandas as pd

filename = "people-100-dirty.csv"

df = pd.read_csv(filename)

print(df.info())
