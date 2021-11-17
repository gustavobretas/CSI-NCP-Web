# Accessing Tuple Elements Using Indexing

# Aim
# In this exercise, you will see how to use indexing to access tuples:

# Steps for Completion
# Create a new pets tuple with the elements dog, cat, and parrot as shown in 
# Snippet 5.22:
# pets = ('dog','cat','parrot')
# Snippet 5.22

# Print pets[1] to access the second index as shown in 
# Snippet 5.23:
# print(pets[1])
# 'cat'
# Snippet 5.23

# Try to print an index that is not in the tuple. Python will raise an IndexError, as shown in 
# Snippet 5.24:
# print(pets[3])
# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#     print(pets[3])
# IndexError: tuple index out of range
# Snippet 5.24

# Indices can also be negative. If you use a negative index, -1 will reference the 
# last element in the tuple, -2 will refer to the second from last element in the tuple, 
# and so on. Use the code shown in 

# Snippet 5.25 to access the tuple:
# pets = 'dog', 'cat', 'parrot', 'gerbil'
 
# print(pets[-1])
 
# print(pets[-2])
 
# print(pets[-3])
# 'gerbil'
# 'parrot'
# 'cat'
# Snippet 5.25

# As with list indices, tuple indices must always be integers, and trying to use 
# other types will result in a TypeError, as shown in Snippet 5.26a and 

# Snippet 5.26b. Type a string and a float value as an index:
# pets = 'dog', 'cat', 'parrot'
# pets['1']
# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#     pets['1']
# TypeError: tuple indices must be integers or slices, not str
# Snippet 5.26a

# pets[1.5]
# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#     pets[1.5]
# TypeError: tuple indices must be integers or slices, not float
# Snippet 5.26b

# The error message presented here mentions slices, and you might be wondering what 
# slices are. This brings us to the alternative way in which you can access tuple 
# elements: slicing.

# Write your code here

#pets = ('dog','cat','parrot')
#print(pets[1])
#print(pets[3])

#pets = 'dog', 'cat', 'parrot', 'gerbil'
#print(pets[-1])
#print(pets[-2])
#print(pets[-3])

#pets = 'dog', 'cat', 'parrot'
#pets['1']
#pets[1.5]

