# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
from numpy import *


csvFoot = open('football.csv', 'r')
data = csv.reader(csvFoot, delimiter=',')
next(data)
data = [row for row in data]
goalsFor = [x[5] for x in data]
goalsAllowed = [x[6] for x in data]
goalsDiff = [float(x) - float(y) for x, y in zip(goalsFor, goalsAllowed)]
Diffs = list(map(lambda x: abs(x), goalsDiff))
minDiff = Diffs.index(min(Diffs))
print(data[minDiff][0])


#The code below is my first attempt at this problem.
#It works, but is not as clean as the code above.
#QUESTION - Why did I need to open the code twice?
"""
#This chunk is used to find the index of the team with the lowest goal differential (minDiff).
with open('football.csv', 'r') as csvFoot:
    readFoot = csv.reader(csvFoot, delimiter=',')
    next(readFoot)
    goalsFor = []
    goalsAllowed = []
    for g in readFoot:
        goalsFor.append(g[5])
        goalsAllowed.append(g[6])
    goalsDiff = [float(x) - float(y) for x, y in zip(goalsFor, goalsAllowed)]
    Diffs = list(map(lambda x: abs(x), goalsDiff))
    minDiff = Diffs.index(min(Diffs))
    
#This chunk finds and prints the team that has the lowest goal differential, using minDiff.   
with open('football.csv', 'r') as csvFoot:
    readFoot = csv.reader(csvFoot, delimiter=',')
    next(readFoot)
    teams = []
    for t in readFoot:
        teams.append(t[0])
    print (teams[minDiff])

#Problems: the dataset appears to be altered whenever it goes through the for loop (parsed?)
"""
