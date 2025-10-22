# This program reads in the "2.1-data.csv" file and outputs each line as a list.
# Author: Marcin Kaminski

import csv

FILENAME = "2.1-data.csv"
# DATADIR = "where did you put it"

# with open (DATADIR + FILENAME, "rt") as fp:
with open(FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter =",")
    for line in reader:
        print(line)
