# Demonstration of calculating basic standard deviation in Python
# Author: Marcin Kaminski

import pandas as pd

# create series
temp1 = pd.Series([56, 65, 78, 86, 88, 92]) # temperatures in Fahrenheit
temp2 = pd.Series([33, 65, 78, 88, 92, 109]) # temperatures in Fahrenheit

# print mean and standard deviation
print(f'temp1: mean = {temp1.mean()}, standard deviation = {temp1.std()}') # default is sample standard deviation
print(f'temp2: mean = {temp2.mean()}, standard deviation = {temp2.std()}') # default is sample standard deviation