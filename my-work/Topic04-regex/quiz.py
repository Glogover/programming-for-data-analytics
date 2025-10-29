# This is code for the quiz
# Author: Marcin Kaminski

import re # for regular expressions

regex = "^Hell?o" # matches any string

filename = "quiz.txt"

with open(filename) as quizFile: # open the file
    for line in quizFile: # read each line
        searchResult = re.search(regex, line) # search for the regex pattern in the line
        if (searchResult): # if there is a match
            matchingLine = line # get the matching line
            print(matchingLine, end="") # print the matching line


"""Quiz answers:
a. hello -->

hello

b. Hello -->

Hello
Hello World
       Hello mary


c. ^Hello -->

Hello
Hello World

d. ^Hell*o -->

Hello
Hello World
Helo John
Helllllllllllo Anamaniacs

e. ^Hell+o -->

Hello
Hello World
Helllllllllllo Anamaniacs
       
f. ^Hell?o -->

Hello
Hello World
Helo John



"""

