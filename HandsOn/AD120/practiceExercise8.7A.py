# Creating, Reading, and Writing to Files

# Aim
# Load a CSV file and count the number of rows in the file.

# Steps for Completion
# In main.py, import the CSV module:

# import csv

# Open the CSV folder as a reader object “f”:

# with open('MOCK_DATA.csv', 'r') as f:
#     mock_data_reader = csv.reader(f)

# After assigning the reader to the CSV file, on the next line within the reader 
# object f, start a line count at 1 and loop through the rows, printing each one as shown in 

# Snippet 8.70:
#     line_count = 1
 
#     for row in mock_data_reader:
#         if line_count > 1: #skipping line 1 which is the header row
#             print(row)
 
#         line_count += 1

# Snippet 8.70

# Your code here
import csv

with open('MOCK_DATA.csv', 'r') as f:
    mock_data_reader = csv.reader(f)
    line_count = 1 
    for row in mock_data_reader:
        if line_count > 1: #skipping line 1 which is the header row
            print(row)
 
        line_count += 1
