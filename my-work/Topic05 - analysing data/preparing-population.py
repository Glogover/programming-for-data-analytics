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

df["Single Year of Age"] = df["Single Year of Age"].str.replace(r"\D","", regex=True) # Remove any non-digit characters using regular expression

#df["Single Year of Age"] = df["Single Year of Age"].astype("Int64") # Convert age to integer type, this throwa an error if there are non-numeric values    
df["Single Year of Age"] = pd.to_numeric (df["Single Year of Age"], errors='coerce').astype("Int64") # Alternative way to convert age to integer type

#df_anal = pd.crosstab(df.loc[:,"Administrative Counties"], df.loc[:, "Single Year of Age"]) # Create a crosstab (cross-tabulation) to summarise population by age for each county

#df_anal = df.pivot_table(df,"VALUE", "Single Year of Age", "Administrative Counties") # Alternative way using pivot table, ths  throws an error !

df_anal = df.pivot_table(values = "VALUE", index = "Single Year of Age", columns = "Administrative Counties", aggfunc="sum") # Alternative way using pivot table, this works !

print (df_anal.head(10)) # Check the data
#print (df.info()) # Check the data types
#df.to_csv("population_for_analysis.csv")
df_anal.to_csv("population_for_analysis.csv")


# End of code

