# This code will find date/time in the smallerAccess.log.txt file
# Author: Marcin Kaminski

import re # for regular expressions

regex = "\[.*\]" # matches anything inside square brackets, this will return the date/time

filename = "smallerAccess.log.txt"

with open(filename) as inputFile:
   for line in inputFile:
       foundTextList = re.findall(regex, line)
       if (len(foundTextList)!= 0):
       #print(foundTextList)
         foundText = foundTextList[0]
       print(foundText)
       # if I did not want the [] at the beginning and end
       print(foundText[1:-1])