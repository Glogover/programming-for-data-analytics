"""In this lab I want to see if there is any relation between the windspeed and the month in Knock. 
I am going to use the dataset
"https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Get the dataset

# 1. Look at the csv file and realise that the first 19 lines do not contain data, so we need to skip them.

df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv")
