import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_months = 0
    net_amount = 0
    open_amount = 0
    close_amount = 0
    net_change = 0
    avg_change = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]
    
    
    for row in csvreader:
        total_months += 1
        net_amount = net_amount + int(row[1])
        if csvreader.line_num-1 == 1:
            open_amount = int(row[1])
        close_amount = int(row[1])
        
        if int(row[1]) >= greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = int(row[1])
        if int(row[1]) <= greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = int(row[1])
        
        
    net_change  = close_amount - open_amount
    avg_change = net_change/(total_months-1)
  
    fileContent = str(f'Total net amount:{net_amount}\n')
    fileContent += str(f'Average Change: {round(avg_change,2)}\n')
    fileContent += str(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n')
    fileContent += str(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})' )
    
    print(fileContent)
    file = open('output.txt',"w")
    file.write(fileContent)
    file.close()
        
