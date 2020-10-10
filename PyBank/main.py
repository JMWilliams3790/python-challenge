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
    greatest_month_inc = ""
    greatest_month_dec = ""


    
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
                greatest_month_inc = row[0]



            if change < greatest_decrease:
                greatest_decrease = change
                greatest_month_dec = row[0]

        previous = int(row[1])
        first_time = False



print("Financial Analysis")
print("----------------------------")
print(f"Total months: {month_count}")
print(f"Total: {total_value}")
print(f"Total Change: {total_change/(month_count-1)}")
print(f"Greatest Increase in Profits: {greatest_month_inc} {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_month_dec} {greatest_decrease}")


output_path = os.path.join("analysis", "results.txt")

f = open(output_path, 'w')

f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total months: {month_count}\n")
f.write(f"Total: {total_value}\n")
f.write(f"Total Change: {total_change/(month_count-1)}\n")
f.write(f"Greatest Increase in Profits: {greatest_month_inc} {greatest_increase}\n")
f.write(f"Greatest Decrease in Profits: {greatest_month_dec} {greatest_decrease}\n")