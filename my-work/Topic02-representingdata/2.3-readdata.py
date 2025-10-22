# This program reads in the "2.1-data.csv" file and outputs each line as a list.
# The program deals with the header line separately.
# Author: Marcin Kaminski

import csv

DATAPATH = "Topic02-representingdata/2.1-data.csv"

with open(DATAPATH, "rt") as fp:
    reader = csv.reader(fp, delimiter =",")
    linecount = 0
    for line in reader:
        if not linecount: # first row ie header row
            print(f"{line}\n-------------------")
        else: # all subsequent rows
            print(line)
        linecount += 1