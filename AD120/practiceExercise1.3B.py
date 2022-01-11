# Aim
# Assign an integer to a variable and then perform mathematical 
# operations with the variable.

# Steps for Completion
# Assign the value 7 to the number variable as shown in Snippet 1.24:
# >>> number = 7
# Snippet 1.24

# We can now use this variable for any operations we'd like. Print out 
# the value of the number variable, multiplied by 5 as shown in Snippet 1.25:
# >>> number * 5
# 35
# Snippet 1.25

# Print out number added to 2 as shown in Snippet 1.26:
# >>> number + 2
# 9
# Snippet 1.26

# Print out number divided by 3.5 as shown in Snippet 1.27:
# >>> number / 3.5
# 2.0
# Snippet 1.27

# Print out number subtracted from itself as shown in Snippet 1.28:
# >>> number - number
# 0
# Snippet 1.28

# Note that, despite having used it, the value of number won't change 
# unless we reassign it. Reassigning 22 to number changes its value as 
# shown in Snippet 1.29:
# >>> print(number)
# 7
# >>> number = 22
# >>> print(number)
# 22
# >>> 
# Snippet 1.29

# You can also assign the resulting value of another operation to a variable. 
# Enter the commands shown in Snippet 1.30:
# >>> number = 7
# >>> x = number + 1
# >>> x
# 8
# >>>
# Snippet 1.30

# String values can also be assigned and used in a similar fashion. First, 
# set the message variable to the string "I love Python" as shown in Snippet 1.31:
# >>> message = "I love Python"
# Snippet 1.31

# Print out the value of the message variable and add an exclamation point 
# at the end as shown in Snippet 1.32:
# >>> message + "!"
# 'I love Python!'
# Snippet 1.32

# Print out message plus three exclamation points as shown in Snippet 1.33:
# >>> message + "!" * 3
# 'I love Python!!!'
# >>>
# Snippet 1.33

# We can see the application of a new operation to strings: + . We use this 
# whenever we want to concatenate (add together) two strings. This only applies 
# to strings, and thus trying to concatenate a string with any other data 
# type will raise an error.

# Write your code here
number = 7
number * 5
number + 2
number / 3.5
number - number
print(number)
number = 22
print(number)
number = 7
x = number + 1
x
message = "I love Python"
message + "!"
message + "!" * 3