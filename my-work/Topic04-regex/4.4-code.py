# This code will find some other regular expressions in the smallerAccess.log.txt file
# Author: Marcin Kaminski

import re # for regular expressions

#regex = ":[0-9:]{8}" # matches a colon followed by exactly 8 digits or colons (this will return the time portion of the date/time)
#regex = "\w+=" # matches any word characters followed by an equals sign (this will return key=value pairs), the variable names in the urls
#regex = "=\w+" # matches an equals sign followed by any word characters (this will return the values in key=value pairs), the variable values in the urls
#regex = "\d+$" # matches one or more digits at the end of a line (this will return the response size in bytes)
regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" # matches an IP address (this will return the IP addresses)


filename = "smallerAccess.log.txt" # the log file to read

with open(filename) as inputFile: # open the file
   for line in inputFile: # read each line
       foundTextList = re.findall(regex, line) # find all matches of the regex pattern in the line
       if (len(foundTextList)!= 0): # if there are any matches
       #print(foundTextList)
         foundText = foundTextList[0] # get the first matching text
       print(foundText) # print the matching text
       # if I did not want the [] at the beginning and end
       #print(foundText[1:-1]) # print the matching text without the first and last character