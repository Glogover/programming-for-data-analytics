# program that reads a file and takes
# Author: Marcin Kaminski

FILENAME = "numbers.txt"

#DATADIR = "../../my-work/"
#FULLPATH = DATADIR + FILENAME

FULLPATH = FILENAME

#print(FULLPATH)

with open(FULLPATH, 'rt') as fp:
    total = 0
    for line in fp:
        print(f"{line.strip()}", end ="") # remove newline
        print(f" has length {len(line)}")
        total += int(line)
    print(total)



