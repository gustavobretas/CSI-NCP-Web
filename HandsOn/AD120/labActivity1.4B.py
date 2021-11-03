# Aim
# Write a script that takes a whole number from a user’s 
# input and prints out its 2's multiplication table till 10.

# Steps for Completion
# Go to your main.py file.

# On the first line, add a docstring explaining what your file does. 
# Then, assign a variable called whole_num to the user’s 
# input and cast it to an integer.

# Next, print 10 underscores as the top border of the table.

# On the first line print your whole number, then multiply your 
# whole number by multiples of 2's till 10 and print that out.

# Finally, print 10 underscores again for the bottom border 
# of the table, as in step 3.

# Run the file by using the python3 main.py command.

# The output should be like Figure 1.10:

# Write your code here
""" This script generates a multiplication table by 2's till 10 for any given number. """ 
whole_num = int(input("Generate a multiplication table for: ")) 
print("_" * 10) 
print("Number:", whole_num)
print("2:", whole_num * 2)
print("4:", whole_num * 4)
print("6:", whole_num * 6)
print("8:", whole_num * 8)
print("10:", whole_num * 10) 
print("_" * 10) 