import numpy
import csv
import re
from collections import Counter

"""
with open('faculty.csv', 'r') as f:
    readF = csv.reader(f)
    data = list(readF)
    for row in data:
        print(row)
"""

csvF = open('faculty.csv', 'r')
data = csv.reader(csvF)
next(data)
data = [row for row in data]


#Q1
degrees = [row[1] for row in data]

degrees.remove('0')

for i in range(len(degrees)): #this removes the spaces in front of the degrees. not doing this would affect how the data is split
    if degrees[i][0] == ' ':
        degrees[i] = degrees[i][1:]
    else:
        pass
degrees = [words for segments in degrees for words in segments.split(' ')] #this splits the data at each space for when professors have multiple degrees. 

for i in range(len(degrees)): #this removes extra spaces and periods, unifying the data
    degrees[i] = degrees[i].replace(' ', '')
    degrees[i] = degrees[i].replace('.', '')

print('There are', len(set(degrees)), 'different degrees.')
print(Counter(degrees))



#Q2
titles = [row[2] for row in data]
for i in range(len(titles)):
    titles[i] = titles[i].replace(' is ', ' of ')
    
print('There are', len(set(titles)), 'different titles.')
print(Counter(titles))



#Q3
emails = [row[3] for row in data]

print(emails)



#Q4
domains = []
for i in range(len(emails)):
    domains.append(emails[i][(emails[i].index('@')+1):])

print('There are', len(set(domains)), 'different domains.')
print(list(set(domains)))
