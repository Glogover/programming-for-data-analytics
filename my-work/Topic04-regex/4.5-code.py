# This code will anonymise the sub domains of ip addresses
# Author: Marcin Kaminski


import re # for regular expressions

#regex = "\d{1,3}\.\d{1,3} " # this will find other numbers apart from ips

regex = "(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}" # matches an IP address, with groups to capture the first two octets
replacementText="\\1XXX.XXX " # we use \\1 to refer to the first group found
filename = "smallerAccess.log.txt" # the log file to read
outputFileName = "anonymisedIPs.txt" # the output file to write

with open(filename) as inputFile: # open the file
   with open(outputFileName, 'w') as outputFile: # open the output file for writing
     for line in inputFile: # read each line 
         # for debuging purposes only
         #foundText = re.search(regex, line).group()
         #print(foundText)
         newLine = re.sub(regex, replacementText, line) # replace the matched ip with the anonymised version
         outputFile.write(newLine) # write the new line to the output file

# End of code
