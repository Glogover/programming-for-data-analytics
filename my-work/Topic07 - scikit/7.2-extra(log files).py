""" This program create a regression plot for the amount of data that was transferred 
for each hour of the day using the data from a log file (access.log.txt)."""

# Author: Marcin Kaminski

import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

""" 
1. This is a function to read in the strings. 
It should strip off the first and last characters.
"""
def parse_str(x):
    return x[1:-1]


""" 
2. This is a function to read in the date in the format it is in the log file.
It will also need to strip the first and last characters (ie the []). 
"""
def parse_datetime(x):
    dt = datetime.strptime(x[1:-1], '%d/%b/%Y:%H:%M:%S')
    return dt


"""
3. Read in the log file into a data frame.
We will not need columns 1 or 2 (they are blank).
Additionally, we need to assign the parsing functions for each column.
"""

df = pd.read_csv(
    'access.log.txt',
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

""" 
4. Check that it was all read in correctly by storing the data frame 
into an excel and looking at it.
"""

excelFilename = 'log.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')

"""
5. Manipulate the columns to get extract data from them e.g. 
you could get more information about the URI and URL
"""
request = df.pop('request').str.split()
df['resource'] = request.str[1]
df['method'] = request.str[0]
#yes I could have used regex for this
# from the request get the string before the ?
df['url'] = request.str[1].str.split('?').str[0]

"""
6. Now lets make another dataframe that stores the sum of 
all the data transferred for each hour (H)
"""
dfbyhour=df.resample('h',on='time').sum()

"""
7.Then make another column in the dataframe for the hour of the day
"""
dfbyhour['hour']=dfbyhour.index.hour
dfbyhour['date']=dfbyhour.index.date

"""
8. Let's make a regression plot for the size of the transfer over the hour of the day
"""
 
sns.lmplot(x="hour", y="size", order=3 ,data=dfbyhour, x_jitter=0.5)

"""
9. Make a plot of the residual to see which order is most appropriate.
(You should try orders 1 to 4 and see which one looks best.)
"""
 
sns.residplot(x="hour", y="size", data=dfbyhour, order=1)

plt.show()
