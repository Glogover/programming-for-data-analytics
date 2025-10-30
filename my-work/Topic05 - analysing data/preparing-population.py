# Preparing the population data for analysis
# The CSO data is quite clean 
# All we really have to do is group it
# Author: Marcin Kaminski

import pandas as pd

FILENAME = "cso-populationbyage.csv"
#DATADIR = "../../data/" # Two levels up from current directory and then into data folder
#FULLPATH = DATADIR + FILENAME

df = pd.read_csv(FILENAME)

drop_col_list = ["Statistic Label","CensusYear","Sex","UNIT"]
#df= df.drop(columns=drop_col_list)
df.drop(columns=drop_col_list, inplace=True)

df = df[df["Single Year of Age"] != "All ages"] # Keep only rows where age is specified
df["Single Year of Age"] = df["Single Year of Age"].str.replace("Under 1 year","0") # Replace "Under 1 year" with "0"

print (df.head(3))
df.to_csv("population_for_analysis.csv")


