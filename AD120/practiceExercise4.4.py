# Creating a Lambda Function

# Aim
# Let's look at a practical application of a lambda function. Suppose that you want to 
# simply sum up two numbers in a function. There is no need to define a whole user-defined 
# function for this if you are only going to use it once.

# Steps for Completion
# Create a lambda function that takes two parameters - first and second as shown in
#  Snippet 4.32:
# answer = lambda first, second : first + second
# print(answer(6, 9))
# Snippet 4.32

# In Snippet 4.32, we have defined a lambda function that takes two parameters 
# (first and second) and adds them up. We have then assigned the function to the answer 
# variable, so that we have a way to refer to it.

# Now, call the function and print out the output, as shown in 
# Snippet 4.33:
# $ python main.py
# 15
# Snippet 4.33

# Write your code here
answer = lambda first, second: first + second

print(answer(6, 9))
