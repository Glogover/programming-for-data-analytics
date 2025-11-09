import pandas as pd
import numpy as number_people

FILENAME = "population_for_analysis.csv"

df = pd.read_csv(FILENAME) # read data from CSV file

#print (df.head(3))
headers = df.columns[1:] # skip first column
print(headers) # get list of districts
district = headers[0] # select first district
# this is incorrect
print(df[district].describe()) # print basic statistics

import numpy as np # import numpy library

w_mean = np.average(df["Single Year of Age"], weights=df[district]) # calculate weighted mean
print(w_mean) # print weighted mean

w_variance = np.average((df["Single Year of Age"] - w_mean)**2, weights=df[district]) # calculate weighted variance
w_std_dev = np.sqrt(w_variance) # calculate weighted standard deviation
print(w_std_dev) # print weighted standard deviation
