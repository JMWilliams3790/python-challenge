import os
import csv


# Find data
csvpath = os.path.join('Resources','budget_data.csv')


# Reading CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvpath, delimiter=',')

    print(csvreader)