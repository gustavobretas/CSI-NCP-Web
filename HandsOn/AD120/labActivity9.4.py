# Creating Your Own Custom Exception Class

# Scenario
# As a developer, you may need to create exception classes that handle 
# custom exceptions that are not defined in the standard library in a certain way.

# Aim
# In this activity, we will practice creating custom exception classes. 
# Use the try… except block to catch user defined errors.

# Steps for Completion
# Go to your main.py file.

# Define an Exception class of your choice and subclass the Exception class as an argument.

# Within your Exception class define the __init__ function to store your error message.

# Write some code where you use the try… except block to capture and handle 
# your custom exception by printing a custom message to the console.

# Running the script with python3 main.py should result in a similar message like the example below:

# Invalid recipe, try again.
# Avoid using the word "error" in your custom message.

# Write your class here
class InvalidRecipeError(Exception): 
    def __init__(self): 
        self.error = "Invalid recipe, try again." 

# Test you custom exception class below
try:
	raise InvalidRecipeError 
except InvalidRecipeError as r: 
    print(r.error) 
