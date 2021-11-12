# Using the for Loop

# Aim

# Working with a practical use of the for loop.

# Steps for Completion
# Open main.py and declare a variable called numbers. We initialize numbers to a 
# list of integers from 1 to 10, as shown in 
# Snippet 3.34:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Snippet 3.34

# Next, loop through the list we just created. Create a new variable called num 
# in the for loop as shown in Snippet 3.35. We will use this variable to represent 
# and access the individual numbers in the list as we loop through it:
# for num in numbers:
# Snippet 3.35

# Inside the loop, calculate the square of num by multiplying it by itself. 
# Note that there are other ways to calculate the square, but this rudimentary method will 
# suffice for our example here. We assign the square of num to the variable square as shown in 
# Snippet 3.36:
#     square = num * num
# Snippet 3.36

# Then, print out the string that tells us that num squared is square as shown in 
# Snippet 3.37:
#     print(num ,' squared is ', square)
# Snippet 3.37

# This loop is repeated for all ten numbers in the list.

# Snippet 3.38 shows the final code with comments added for clarification:

# # Create a list with numbers 1 through 10
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# # Loop through the list of numbers 
# for num in numbers:
#     # Calculate the square of the number
#     square = num * num
#     # Print out a string showing the number and its calculated sqaure
#     print(num, `squared is`, square)
# Snippet 3.38

# Run the script. The output is shown in Snippet 3.39:

# $ python main.py

# 1 squared is 1
# 2 squared is 4
# 3 squared is 9
# 4 squared is 16
# 5 squared is 25
# 6 squared is 36
# 7 squared is 49
# 8 squared is 64
# 9 squared is 81
# 10 squared is 100
# Snippet 3.39

# As expected, the loop iterates over the list numbers, calculates the square of 
# each number, and prints out the result in a readable format.

# Write your code here
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    square = num * num
    print(num ,' squared is ', square)
