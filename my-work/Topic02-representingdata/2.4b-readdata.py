# The program calculates the average age using quote parameter to read in the numbers as floats.
# Author: Marcin Kaminski

import csv

DATAPATH = "Topic02-representingdata/2.1-data.csv"

with open(DATAPATH, "rt") as fp:
    reader = csv.reader(fp, delimiter =",", quoting = csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row ie header row
            pass
        else: # all subsequent rows
            total +=line[1] # age is the second column
        linecount += 1
    print(f"average is {total/(linecount-1)}") # subtract 1 to exclude header row
    