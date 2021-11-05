# Aim

# Practice converting between different types of number systems. 
# We will create a script that takes the user's input and converts 
# it into a binary number.

# Steps for Completion
# First, define the number variable that takes a user input:
# number = input("Convert to binary: ")
# Convert the input to an integer:
# # convert number to integer
# integer = int(number)
# Then, convert it to a binary number:
# # convert integer to binary
# binary = bin(integer)
# Finally, print out the value:
# print(binary)
# The final script should resemble Snippet 2.9 shown below:

# In [1]: number = input("Convert to binary: ")                                                                                                                               
# Convert to binary: 9
# # convert number to integer
# In [2]: integer = int(number)                                                                                                                                              
# # convert integer to binary
# In [3]: binary = bin(integer)                                                                                                                                               
# In [4]: print(binary)                                                                                                                                                       
# 0b1001
# Snippet 2.9

# The running script should look like the one shown in Figure 2.1:
# converting-between-different-number-systems
# Figure 2.1

# When a number in preceded by 0b it indicates the number is in 
# binary notation. If the number is preceeded by 0x it is in hex notation.

# Write your code here
number = input("Convert to binary: ")
# convert number to integer
integer = int(number)
# convert integer to binary
binary = bin(integer)
print(binary)