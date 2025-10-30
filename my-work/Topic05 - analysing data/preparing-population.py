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
df.drop(columns=drop_col_list, inplace=True)

print (df.head(3))


