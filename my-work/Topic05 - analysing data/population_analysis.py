# Analysing population wrong
# Author: Marcin Kaminski

import pandas as pd

FILENAME = "population_for_analysis.csv"

df = pd.read_csv(FILENAME)

print(df.head(3))
