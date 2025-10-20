# Reads in the iris data set as json
# Author: Marcin Kaminski

import json

FILENAME = "iris.json"
# DATADIR = "../../data/"
# FULLPATH = DATADIR + FILENAME
FULLPATH = FILENAME

with open(FULLPATH, "r") as fp:
    irisdataset = json.load(fp)
    print(irisdataset)
    #print(irisdataset[0])
    