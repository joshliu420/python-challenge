import os
import csv

# create function to do the calculation
def PyBank_analysis(csvfile, profit_data):
    # the number of months = the number of rows
    months = len(list(profit_data))
    
    # reset the loop
    csvfile.seek(0)
    next(profit_data)

    # sum the value in "Profit/Losses" Column
    total = 0
    for row in profit_data:
        total += float(row[1])

    # reset the loop
    csvfile.seek(0)
    next(profit_data)

    # create a list for column "Profit/Losses" for furthur calculation
    profit_list = []
    month_list = []
    for row in profit_data:
        profit_list.append(row[1])
        month_list.append(row[0])
    
    # calculate the avg change
    avg_change = (float(profit_list[-1]) - float(profit_list[0])) / 85

    # reset the loop
    csvfile.seek(0)
    next(profit_data)

    # create a list to store the changes for each month
    changes_list = []
    for row in range(1,len(profit_list)):
        changes = float(profit_list[row]) - float(profit_list[row-1])
        changes_list.append(changes)

    # find the max & min number for changes
    max_change = max(changes_list)
    min_change = min(changes_list)

    # locate the position of the max & min changes and find out the relevant position in month_list
    max_month = month_list[changes_list.index(max(changes_list))+1]
    min_month = month_list[changes_list.index(min(changes_list))+1]
  
    # reset the loop
    csvfile.seek(0)
    next(profit_data)
    
    # print out the result
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {max_month} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_month} (${min_change})')

    # set up the output path and prepare to export the result
    output_path = os.path.join("PyBank_output.txt")
    with open(output_path, 'w', newline='') as txtoutput:

        # Initialize csv.writer
        txtwriter = csv.writer(txtoutput, delimiter=',')

        # Write row by row
        txtwriter.writerow(['Total Month', str(months)])
        txtwriter.writerow(['Total', '$'+str(total)])
        txtwriter.writerow(['Average Change', '$'+str(avg_change)])
        txtwriter.writerow(['Greatest Increase in Profits', str(max_month), '$'+str(max_change)])
        txtwriter.writerow(['Greatest Decrease in Profits', str(min_month), '$'+str(min_change)])
        

# open the file and use the function
PyBank_path = os.path.join('Resources', 'budget_data.csv')

with open(PyBank_path,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    PyBank_analysis(csvfile,csvreader)