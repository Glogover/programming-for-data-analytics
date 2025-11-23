"""In this lab I want to see if there is any relation between the windspeed and the month in Knock. 
I am going to use the dataset
"https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv"""
# Author: Marcin Kaminski

# *** Import the libraries ***


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


# 3. If you look at the data you will see that there are some windspeeds missing, we need to drop those rows, lets make a new dataset which only has the month and wind speed.

# https://stackoverflow.com/questions/29314033/drop-rows-containing-empty-cells-from-a-pandas-dataframe

# 4. Great, now lets drop the NAs

cleandf = df[["month", "wdsp"]] # make a new dataframe with only the month and windspeed
# replace the spaces with NaN
cleandf['wdsp'] = cleandf['wdsp'].replace(' ', np.nan)
cleandf.dropna(inplace=True) # drop the rows with NaN values

# print(cleandf.head(3)) # check the new dataframe

# 5. Now we just need to convert the wind speed to floats
cleandf["wdsp"] = cleandf["wdsp"].astype(float) # convert the wind speed to floats

# *** Now we can analyse ***

# 6. Is there any correlation between the windspeed and the month?

corrwind = cleandf["month"].corr(cleandf["wdsp"])
print(f"The correlation between the month and the windspeed is: {corrwind}")
# The answer is still no, but we can visualise the data to see if there is any pattern. 
# The reason for no correlation is the same as before, the month is cyclical and the windspeed is affected by the year.











