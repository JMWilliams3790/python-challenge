import os
import csv

# Find data
csvpath = os.path.join('Resources','budget_data.csv')


# Reading CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Define header
    csv_header = next(csvreader)
    #Find total value
    month_count = 0
    total_value = 0
    change = 0
    for row in csvreader:  
        month_count += + 1   
        total_value += int(row[1])
    



print("Financial Analysis")
print("----------------------------")
print(f"Total months: {month_count}")
print(f"Total: {total_value}")