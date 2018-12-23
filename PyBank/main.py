#########################################
# Analyzing Financial Records of PyBank #
#########################################

import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join("", "Resources","budget_data.csv")

# Read the csv file
with open(pybank_csv, newline="")as csvfile:

    # Split the data on commas
    pybank_csv = csv.reader(csvfile,delimiter=",")

    # Get the first row and store in header to skip and go to next row
    header = next(pybank_csv)

    # Initialize the row counter to 0
    rowcounter = 0

    # Initialize the total_budget to 0
    total_budget = 0

    # Set variable list for dateVal, profit_loss, rev_change
    dateVal =[]

    profit_loss = []

    rev_change = []

    # Loop through the data in pybank_csv row by row
    for data in pybank_csv:

        # Get the total from index data element 1 and store in variable total
        total = int(data[1])

        # Sum the total and add to total_budget
        total_budget+=total

        # Add 1 to rowcounter to move to next row
        rowcounter+=1
        
        # Get total value and append to profit_loss list
        profit_loss.append(total)
        
        # Get date and append to dateVal list
        dateVal.append(data[0])

# from range 0 to total row -1, calculate revenue change between element [i+1] and  element i        
for i in range(0, rowcounter - 1):
    rev_change.append(int(profit_loss[i+1]) - int (profit_loss[i]))

# calculate average_change
average_change = round(sum(rev_change)/len(rev_change),2)

# get the maximum revenue change
maximum = max(rev_change)

# get the index of element with maximum revenue change
max_index = rev_change.index(maximum) + 1

# get the date with maximum revenue change
date_max = dateVal[max_index]

# get the minimum revenue change
minimum = min(rev_change)

# get the index of element with minimum revenue change
min_index = rev_change.index(minimum) + 1

# get the date with minimum revenue change
date_min = dateVal[min_index]

######  print your analysis  ######
print("------------------------------------------------------") 
print("Financial Analysis")
print("------------------------------------------------------")  
print("Total Months : " + str(rowcounter)) 
print("Total : $" + str(total_budget))
print("Average Change : $" + str(average_change) )
print("Greatest Increase in Profits : " + str(date_max) + "($" + str(maximum) + ")")
print("Greatest Decrease in Profits : " + str(date_min) + "($" + str(minimum) + ")")
print("------------------------------------------------------")