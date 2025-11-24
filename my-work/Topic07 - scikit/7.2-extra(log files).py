""" This program create a regression plot for the amount of data that was transferred 
for each hour of the day using the data from a log file (smallerAccess.log)."""

# Author: Marcin Kaminski

import pandas as pd
import datetime as dt
import seaborn as sns

""" 1. This is a function to read in the strings. It should strip off the first and last characters."""

def parse_str(x):
    return x[1:-1]  

""" 2. This is a function to read in the date in the format it is in the log file.
It will also need to strip the first and last characters (ie the []). """

def parse_datetime(x):
    dt = dt.strptime(x[1:-1], '%d/%b/%Y:%H:%M:%S')
    return dt

"""
3. Read in the log file into a data frame.
We will not need columns 1 or 2 (they are blank).
Additionally, we need to assign the parsing functions for each column.."""

df = pd.read_csv(
    'smallerAccess.log.txt',
    sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
    engine='python',
    na_values='-',
    header=None,
    usecols=[0, 3, 4, 5, 6, 7, 8],
    names=['ip', 'time', 'request', 'status', 'size', 'referer',
'user_agent'],
    converters={'time': parse_datetime,
                'request': parse_str,
                'status': int,
                'size': int,
                'referer': parse_str,
                'user_agent': parse_str})

""" 4. check that it was all read in correctly by storing the data frame 
into an excel and looking at it.
"""

excelFilename = 'smallerAccess.log.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')