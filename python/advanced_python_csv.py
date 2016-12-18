import numpy
import csv

csvF = open('faculty.csv', 'r')
data = csv.reader(csvF)
next(data)

emails = [row[3] for row in data]

with open('emails.csv', 'w') as file:
    write = csv.writer(file)
    write.writerows(zip(emails))
