#budget

import os
import csv

budget_csv = os.path.join("resources", "budget_data.csv")
# "C:\Users\alyss\OneDrive\Desktop\Python\python_challenge\pybank\resources"

#list that stores data
months= []
profitloss= []
changes= []

#variables set to 0
totalmonths= 0
totalprofitloss= 0
previousloss= 0



# with open csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header= next(csvreader)
    


    for row in csvreader:

        months.append(row[0])
        profitloss.append(int(row[1]))

        #total months and net total of profit/losses
        totalmonths= len(months)
        totalprofitloss= sum(profitloss)

        #changes of profit/losses and the average of those changes
        profit_loss = int(row[1])
        change = profit_loss - previousloss
        changes.append(change)
        previousloss = profit_loss
        average = sum(changes)/len(changes)

        #greatest increase and decrease in profits (date and amount)
        increaseprofit= max(changes)
        decreaseprofit= min(changes)
        increasemonth= months[changes.index(increaseprofit)]
        decreasemonth= months[changes.index(decreaseprofit)]

#print results 
print("                          ")
print("Financial Analysis")
print("                          ")
print("--------------------------")
print("Total Months: " + str(totalmonths))
print("Total: $" + str(int(totalprofitloss)))
print(f"Average Change: ${average: .2f}")
print(f"Greatest Increase in Profits: {increasemonth} (${increaseprofit})")
print(f"Greatest Decrease in Profits: {decreasemonth} (${decreaseprofit})")

#export to a text file
with open("budget_analysis.txt", "w") as text:
    text.write("                          \n")
    text.write("Financial Analysis\n")
    text.write("                          \n")
    text.write("--------------------------\n")
    text.write("Total Months: " + str(totalmonths) + "\n")
    text.write("Total: $" + str(int(totalprofitloss)) + "\n")
    text.write(f"Average Change: ${average: .2f}\n")
    text.write(f"Greatest Increase in Profits: {increasemonth} (${increaseprofit})\n")
    text.write(f"Greatest Decrease in Profits: {decreasemonth} (${decreaseprofit})\n")