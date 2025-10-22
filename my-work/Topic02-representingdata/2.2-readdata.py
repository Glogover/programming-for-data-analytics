import csv

FILENAME = "2.1-data.csv"
# DATADIR = "where did you put it"

with open(FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter =",")
    for line in reader:
        print(line)
        