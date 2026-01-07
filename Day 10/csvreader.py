import csv
with open("Day 10/Student.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)  