# This program reads in the "2.1-data.csv" file and outputs each line as a list.
# Author: Marcin Kaminski

import csv
#import os

#print("Current working directory:", os.getcwd())

#FILENAME = "2.1-data.csv"
#DATADIR = "../..//Topic02-representingdata/"
DATAPATH = "Topic02-representingdata/2.1-data.csv"


# with open (DATADIR + FILENAME, "rt") as fp:

with open(DATAPATH, "rt") as fp:
    reader = csv.reader(fp, delimiter =",")
    for line in reader:
        print(line)
