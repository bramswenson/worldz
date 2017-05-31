# python is dead, long live python 
# (you should be using python3, which is why people 
#  are leaving beautiful soup i found out, no py3 support)
from __future__ import print_function

import sys
import collections
import csv
import random


# Contants are just that, constant to the program
MAP = collections.defaultdict(dict)

# made detfile a required initalization arg
class Location:
    def __init__(self, name, detfile):
        self.name = name
        with open(detfile, 'rb') as details:
            info = csv.DictReader(details)
            for row in info:
                if name == row["name"]:
                    self.description = row["desc"]
                    self.maxMobs = row["maxMobs"]
                    self.maxMobLvl = row["maxMobLvl"]

    number = 0
    name = ""
    description = ""
    maxMobs = 0
    maxMobLvl = 0



# make the core code a callable function that takes options for the
# map and details files paths, again required without any defaults
def main(mapfile, detfile):
    cols = rows = 0

    with open(mapfile, 'rb') as mapdata:
        #set current to [0][0]
        curA = curB = 0

        scanner = csv.reader(mapdata)
        #for each row in the csv
        for row in scanner:
            #for each column in the row
            for col in row:
                #write a field of the csv to the map
                MAP[curA][curB] = Location(col, detfile)
                #debug: display coordinates
                #print "%d:%d - %s" %(curA, curB, MAP[curA][curB])
                if curA == 0:
                    cols += 1
                #move to the next column in the map
                curB += 1
                1
            #move to the next row in the map
            curA += 1
            rows +=1
            curB = 0


    #movement test
    print("Columns: %d" % cols)
    print("Rows: %d" % rows)
    curA = random.randrange(1, 5, 1)
    curB = random.randrange(1, 5, 1)
    while True:

        print("\n\nYou are currently at: %d: %d - %s" % (curA, curB, MAP[curA][curB].name))
        print(MAP[curA][curB].description)
        if curB < cols-1 and MAP[curA][curB+1].name != '':
            print("To the East is %s " % MAP[curA][curB+1].name)
        if curB > 0 and MAP[curA][curB-1].name != '':
            print("To the West is %s " % MAP[curA][curB-1].name)
        if curA < rows-1 and MAP[curA+1][curB].name != '':
            print("To the South is %s " % MAP[curA+1][curB].name)
        if curA > 0 and MAP[curA-1][curB].name != '':
            print("To the North is %s " % MAP[curA-1][curB].name)

        move = raw_input("Which way?  ")
        try:
            if move[0].capitalize() == "N" and curA > 0 and MAP[curA-1][curB].name != '':
                curA -= 1
            elif move[0].capitalize() == "S" and curA < rows - 1 and MAP[curA+1][curB].name != '':
                curA += 1
            elif move[0].capitalize() == "E" and curB < cols - 1 and MAP[curA][curB+1].name != '':
                curB += 1
            elif move[0].capitalize() == "W" and curB > 0 and MAP[curA][curB-1].name != '':
                curB -= 1
            else:
                print("You can't go that way!")
        except:
            print("I don't understand...")


    #write until first , to current
    #if end of line, set current to [+1][0]
    #else set current to [0][+1]


# only run the program when called from the command line
# this allows this file to be executed or imported
# before if imported, it would also execute
# which is typically not a welcome side effect
if __name__ == "__main__":
    # grab arguments from the command line if they exist
    # sys.argv[0] is the name of the executed file 
    # (typically, depending on how it was called)
    if next(iter(sys.argv[1:]), None):
        mapfile = sys.argv[1]
    else:
        mapfile = "data/testmap.csv"
    if next(iter(sys.argv[2:]), None):
        detfile = sys.argv[2]
    else:
        detfile = "data/mapDetail.csv"

    main(mapfile, detfile)
