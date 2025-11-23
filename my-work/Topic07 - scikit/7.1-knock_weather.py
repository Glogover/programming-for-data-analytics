"""In this lab I want to see if there is any relation between the windspeed and the month in Knock. 
I am going to use the dataset
"https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# *** Get the dataset ***

# 1. Look at the csv file and realise that the first 19 lines do not contain data, so we need to skip them.

df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", skiprows=19)
print(df.head(3))

# 2. Is there any correlation between the mean temperature and the month?

corrtemp = df["month"].corr(df["meant"])
print("The correlation between the month and the mean temperature is:", corrtemp)

# The answer is no, but that is for a number of reasons:
# 1. The month is not a continuous variable, it is cyclical (after December comes January again)
# 2. The temperature is also affected by the year, so we need to take that into account.
# 3. There are missing values in the dataset, which can affect the correlation. 

# *** Tidy the wind data ***






