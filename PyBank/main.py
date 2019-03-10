import os

import csv

csvpath = ('budget_data.csv')

with open(csvpath, 'r') as file_handler:
   reader = csv.reader(file_handler)
   next(reader)
   
total_months =  0
total_profitsloss = 0
profitsloss_changes = []
previous_profitsloss = None
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = None
greatest_decrease_month = None


for row in reader:
      current_month = row[0]
      current_profitsloss = int(row[1])

      total_months = total_months + 1
      total_profitsloss = current_profitsloss + int(row[1])

if previous_profitsloss:
   profitsloss_change = current_profitsloss - previous_profitsloss
   profitsloss_changes.append(profitsloss_change)

if profitsloss_change > greatest_increase:
   greatest_increase = profitsloss_change
   greatest_increase_month = current_month
if profitsloss_change < greatest_decrease:
   greatest_decrease = profitsloss_change
   greatest_decrease_month = current_month

previous_profitsloss = current_profitsloss

average_change = sum(profitsloss_changes) / len(profitsloss_changes)

print('Total Months: %d'% total_months)
print('Total Profit Loss: %d'%total_profitsloss)
print('Average Change: %.2f'%averange_change)
print('Greatest Increase in Profits: %s (%d)'%(greatest_increase_month, greatest_increase)
print('Greatest Decrease in Profits: %s (%d)'%(greatest_decrease_month, greatest_decrease)

def(main)
   f= open("Financial_Analysis.txt","w+")


