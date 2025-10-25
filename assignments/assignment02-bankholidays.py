# This program prints out the dates of the bank holidays that happen in Northern Ireland.
# Author: Marcin Kaminski

import json

FILENAME = 'ukbankholidays.json'

with open(FILENAME, 'rt') as file:
    for line in file:
        print(line, end="")
        