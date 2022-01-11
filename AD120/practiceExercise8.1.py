# Creating Modules

# Aim
# In this exercise, we are creating a user-defined module which will print 
# the different musical note lengths.

# Steps for Completion
# To create a module, first check if the module already exists. If it exists, 
# then create the module with a different name.

# Import the musicalnote module, as shown in 

# Snippet 8.3:
# >>> import musicalnote
# Snippet 8.3

# The error message is shown in 

# Snippet 8.4:

# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'musicalnote'
# Snippet 8.4

# The module does not exist; now create a module with the name musicalnote.

# Create a file musicalnote.py that prints the different lengths of musical notes. 

# The file is shown in Snippet 8.5:

# def listnote():
#  print("Whole note, Half note, Quarter note, Eighth note, and Sixteenth note")
# Snippet 8.5

# Import the module and print the values as shown in Snippet 8.6:

# >>> import musicalnote
# >>> musicalnote.listnote()
# Snippet 8.6

# The output is as shown in Snippet 8.7:

# Whole note, Half note, Quarter note, Eighth note, and Sixteenth note
# Snippet 8.7

# We have successfully created a new module musicalnote which prints the name of the musical notes.

# Your code here
# Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
>>> import musicalnote
>>> musicalnote.listnote()
>>>