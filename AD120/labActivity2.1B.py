# Scenario

# You are given the number of days that you have been driving, 
# and you will write a Python script to work out the equivalent 
# number of years and weeks.

# Aim
# Write a script that takes user input as days and converts 
# the days into years, weeks, and days, and then prints them out. 
# We can ignore leap years. The aim of this activity is to use 
# different arithmetic operators to split days into years, weeks, 
# and days.

# Steps for Completion
# Go to your main.py file.

# On the first line, ask the user how many days they've been driving 
# for and declare the user input. It's an integer, so cast the string.

# Then calculate the number of years in that set of days.

# Next, convert the remaining days that weren't converted to years into weeks.

# Then, get any remaining days that weren't converted to weeks.

# Print everything out.

# Finally, run the script with the python3 main.py command.

# The output should look like Figure 2.5 shown below:
# How many days have you been driving? 1000
# You have been driving for:
# Years: 2
# Weeks: 38
# Days: 4

# Write your code here
daysDriving = int(input("Days you have been driving? "))
yearsDriving = daysDriving//365
remainingDaysYears = daysDriving%365
weeksDriving = remainingDaysYears//7
remainingDaysWeeks = remainingDaysYears%7

print("You have been driving for:")
print("Years:", yearsDriving)
print("Weeks:", weeksDriving)
print("Days:", remainingDaysWeeks)