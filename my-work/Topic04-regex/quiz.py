# This is code for the quiz
# Author: Marcin Kaminski

import re # for regular expressions

regex = ".*" # matches any string
#regex = "hello" # matches 'hello'
#regex = "Hello" # matches 'Hello'
#regex = "^Hello" # matches 'Hello' at the beginning of a line
#regex = "^Hell*o" # matches 'Helo', 'Hello', 'Helllo
#regex = "^Hell+o" # matches 'Hello', 'Helllo', 'Hellllo', etc.
#regex = "^Hell?o" # matches 'Helo' or 'Hello'
#regex = "^hello [A-Z]" # matches 'hello ' followed by a capital letter at
#regex = "^Hello [A-Z]" # matches 'Hello ' followed by a capital letter at
#regex = "= " # matches '= ' (equals sign followed by a space)
#regex = "# " # matches '# ' (hash sign followed by a space)
#regex = "[ " # invalid regex pattern (unterminated character set)
#regex = "^$" # matches an empty line



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

g. ^hello [A-Z] -->

no matches


h. ^Hello [A-Z] -->

Hello World


i. =  -->

var = 123

j. # -->

change this #this will change

k. [  -->

no matches

re.error: unterminated character set at position 0

l. ^$ -->

no matches


"""

