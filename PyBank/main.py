 
import os
import csv
 
profits = 0
Greatest_Increase = 0 # 1170593 is the highest value
Biggest_Decrease = 0  #  -1196225 is the lowest value
Total_Months = []
Total_Profits = []
Monthly_Change = []
 
dates = []
value = []
 
csvpath = os.path.join('..' ,'RUTJC201904DATA3/hw/week3/Instructions/PyBank/Resources/budget_data.csv')
with open(csvpath, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
 
  
    highest_value = 0
    next(csv_reader)  # Header does not print
    for row in csv_reader:
        # print(row)
        dates.append(row[0])
        value.append(int(row[1]))
        # print(value)
        profits = int(row[1]) + profits
        # print(profits)
       
Total_Months = len(dates)
 
Total_Profits = str(profits)
 
change = []
 
for i in range(len(value)-1):
    change.append (value[i+1]-value[i])
   
   
Min = min(change)
Max = max(change)
date_min = dates[change.index(Min)+1]
date_max = dates[change.index(Max)+1]
avg_change = sum(change)/len(change)
 
 
 
 
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(Total_Months))
print("Total: " + str(Total_Profits))
print ("Average Change " + '$'+str(round(avg_change,2)))
print("Greatest Increase in Profits: " + date_max + " $"+str(Max))
print("Greatest Decrease in Profits: " + date_min + ' ($'+str(abs(Min))+')' )
 

f = open("main.txt", "w")
	
f.write(
	"Financial Analysis\n"   +
	"Total Months "  + str(len(dates))+ '\n' +
	"Total " + str(sum(value)) + '\n' +
	"Average Change $" +str(round(sum(change)/len(change))) +'\n'+
	"Greatest Increase in Profits $" +str(max(value)) +'\n' +
	"Greatest Decrease in Profits " + '($'+str(abs(Min))+')' 
	)
f.close()         
