import os
import csv
import statistics
budget_csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
budget_output=os.path.join('..', 'Resources','pybank_result_summary.txt')

# Initialize values 
month_count = 0
net_p_and_l = 0
net_delta_p_and_l = []
greatest_increase = ["",0]
greatest_decrease = ["",10E10]

with open(budget_csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        print(csvreader)

#  header 
        csv_header = next(csvreader)

# counting no of months 
        first_row = next(csvreader)
        month_count += 1
        net_p_and_l += int(first_row[1])

#first row            
        previous_row = int(first_row[1])

        for row in csvreader:
                month_count = month_count + 1
                net_p_and_l += int(row[1])

                delta_p_and_l = int(row[1])-previous_row
                previous_row = int(row[1])
                net_delta_p_and_l += [delta_p_and_l]

# increase array with its index 
                if delta_p_and_l > greatest_increase[1]:
                        greatest_increase[0] = row[0]
                        greatest_increase[1] = delta_p_and_l
        
                if delta_p_and_l < greatest_decrease[1]:
                        greatest_decrease[0] = row[0] 
                        greatest_decrease[1] = delta_p_and_l
        
average = round(sum(net_delta_p_and_l)/len(net_delta_p_and_l),2)

                      

print_content = ("Financial Analysis\n")
print("------------------------\n")
print(f"Total Months: {month_count}\n")
print(f"Total: {net_p_and_l}\n")
print(f"Average  Change: ${average}\n")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print_content = (f"Financial Analysis\n"

                 f"------------------------\n"
                 f"Total Months: {month_count}\n"
                 f"Total: {net_p_and_l}\n"
                 f"Average  Change: ${average}\n"
                 f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
                 f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

with open(budget_output, "w") as text_file:
        text_file.write(print_content)