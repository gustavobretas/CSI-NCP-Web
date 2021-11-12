# Defining Global and Local Variables

# Aim

# Define global and local variables. We will also demonstrate the 
# difference between global and local variables.

# Steps for Completion
# First, declare and initialize number to 5 as shown in 
# Snippet 4.6:
# number = 5
# Snippet 4.6

# Then, define a function called summation that takes two named parameters 
# first and second as shown in 
# Snippet 4.7:
# def summation(first, second):
# Snippet 4.7

# Inside of the function, add up the two parameters that were passed in and the 
# global variable number as shown in 
# Snippet 4.8:
#     total = first + second + number
# Snippet 4.8

# Return the final total as shown in Snippet 4.9:
#     return total
# Snippet 4.9

# Call the summation function with two parameters, as expected (10 and 20) as shown in 
# Snippet 4.10:
# summation(10, 20)
# Snippet 4.10

# Print out the initial value of the number as shown in 
# Snippet 4.11:
# print("The first number we initialized was " + str(number))
# Snippet 4.11

# Try to access the local variable total as shown in 
# Snippet 4.12:
# print("The total after summation is " + str(total))
# Snippet 4.11

# Note the use of the built-in function, str(), which returns the string version of an object.

# The final code should resemble Snippet 4.13 shown below:

# # Initialize global variable "number" to 5
# In [1]: number = 5                                                                                                                                                   
# """
# Define function "summation" that takes two parameters
# Note that the function accesses the global variable "number"
# """
# In [2]: def summation(first, second):
#    ...:     # Add the parameters and global number together
#    ...:     total = first + second + number
#    ...:     # Return result
#    ...:     return total 
#    ...:                                                                                                                                                              
 
# In [3]: summation(10, 20)                                                                                                                                            
# Out[3]: 35
 
# # Print out the initial value of "number"
# In [4]: print("The first number we initialized was " + str(number))                                                                                                  
# The first number we initialized was 5
 
# # Try to access the local variable "total"
# In [5]: print("The total after summation is " + str(total))  
# Snippet 4.13

# Running this code will produce the output shown in Snippet 4.14 below:

# NameError                                 Traceback (most recent call last)
# <ipython-input-5-f97c51e0e982> in <module>
# ----> 1 print("The total after summation is " + str(total))

# NameError: name 'total' is not defined
# Snippet 4.14

# As you can see, this results in an error, because we are trying to access the local 
# variable total from the global scope. This is just to demonstrate that we cannot 
# access local variables globally.

# Now, change the code shown in Snippet 4.15; we will get different output upon 
# calling the function:
# # Initialize global variable "number" to 5
# In [1]: number = 5                                                                                                                                                   
# """
# Define function "summation" that takes two parameters
# Note that the function accesses the global variable "number"
# """
# In [2]: def summation(first, second):
#    ...:     # Add the parameters and global number together
#    ...:     total = first + second + number
#    ...:     # Return result
#    ...:     return total 
#    ...:                                                                                                                                                              
 
# # Call the "summation" function with two parameters as excepted
# # Assign the result of "summation" to the variable "outer_total
# In [3]: outer_total = summation(10, 20)                                                                                                                              
 
# # Print out the initial value of "number"
# In [4]: print("The first number we initialized was " + str(number))                                                                                                  
# The first number we initialized was 5
 
# # Try to access the local variable "total"
# In [5]: print("The total after summation is " + str(outer_total))                                                                                                    
# The total after summation is 35
# Snippet 4.15

# Notice that we are now assigning the result of the summation function to the outer_total variable.

# The output now changes to what we expect, without errors, and it looks like 
# Snippet 4.16:

# The first number we initialized was 5
# ...
# The total after summation is 35
# Snippet 4.16

# Write your code here --> Run the code on Compiler, line by line
number = 5
def summation(first, second):
    total = first + second + number
    return total

summation(10, 20)
print("The first number we initialized was " + str(number))
print("The total after summation is " + str(total))

outer_total = summation(10, 20)                                                                                                                              
print("The first number we initialized was " + str(number))                                                                                                  
print("The total after summation is " + str(outer_total))                                                                                                    


