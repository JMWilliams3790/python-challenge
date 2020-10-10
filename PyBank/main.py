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
    first_value = 0
    next_value = 0
    change = 0
    total_change = 0
    first_time = True
    greatest_increase = 0
    greatest_decrease = 999999999


    
    for row in csvreader:
        change = int(row[1])  
        month_count += 1   
        total_value += int(row[1])


        if not first_time:
            change = int(row[1]) - previous
            total_change += change

            #if current change is greater than previous change then greater change = current
            if change > greatest_increase:
                greatest_increase = change

            if change < greatest_decrease:
                greatest_decrease = change

        previous = int(row[1])
        first_time = False



print("Financial Analysis")
print("----------------------------")
print(f"Total months: {month_count}")
print(f"Total: {total_value}")
print(f"Total Change: {total_change/(month_count-1)}")
print(greatest_increase)
print(greatest_decrease)