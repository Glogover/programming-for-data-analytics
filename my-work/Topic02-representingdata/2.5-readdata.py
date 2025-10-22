# The program calculates the average age using quote parameter to read in the numbers as floats.
# The CVS file is read in as a dictionary object using DictReader()
# Author: Marcin Kaminski

import csv

DATAPATH = "Topic02-representingdata/2.1-data.csv"

with open(DATAPATH, "rt") as fp:
    reader = csv.DictReader(fp, delimiter =",", quoting = csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line["age"] # age is the second column
        # print(line)
        count += 1

    print(f"average is {total/count}") # count is already excluding header row
    