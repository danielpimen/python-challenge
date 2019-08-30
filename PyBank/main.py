#The total number of months included in the dataset
import os
import csv
budget_csv = os.path.join("budget_data.csv")
print("Working")
file = open(budget_csv)
numline = len(file.readlines())
print (int(numline - 1))

#The net total amount of "Profit/Losses" over the entire period
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    for row in csvreader:
        print(row)
#The average of the changes in "Profit/Losses" over the entire period


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period