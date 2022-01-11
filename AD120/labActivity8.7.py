# Introduction

# Scenario
# You are an HR manager and you need to create a file containing wages for 
# your employees calculated by their hours.

# Aim
# Read in a CSV file with the employee names and the hours worked, and then 
# output another CSV file with their pay_rate calculated with the rate 1 hour * 15.

# Steps for Completion
# Go to your main.py file.

# Using the csv imported module, write a script to read the contents of our 
# employees.csv file that has the format shown in Figure 8.5:

# employee_name,hours_worked
# John Henry,38
# Maria Gray,43
# Larry Simon,35

# Figure 8.5

# Output a new CSV file called wages.csv which should have the format shown in Figure 8.6:

# employee_name,pay_rate
# John Henry,570
# Maria Gray,645
# Larry Simon,525

# Figure 8.6

# Here, wages are calculated using the formula, hours_worked * 15.

# Make sure you've generated the output file by running python3 main.py and then verify that the content follows the correct format by clicking on the wages.csv file in your editor.

# Your output file does not need to include a $.

# Write your code here
import csv

output_data = []

with open('employees.csv', 'r') as f:
    mock_data_reader = csv.reader(f)
    output_data = []
    line_count = 1

    for row in mock_data_reader: 
        if line_count != 1:
            row[1] = int(row[1]) * 15
            output_data.append(row)

        line_count += 1

with open('wages.csv', 'w') as f:
    fields = ['employee_name', 'pay_rate']
    output_writer = csv.DictWriter(f, fieldnames=fields)

    output_writer.writeheader()

    for line in output_data:
        output_writer.writerow(
            {
              'employee_name': line[0],
              'pay_rate': line[1]
            }
        )

