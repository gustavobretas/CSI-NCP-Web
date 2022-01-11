# Listing the Resources Defined in a Package or Module

# Scenario
# You are implementing a program at work and you need to use a package 
# that you have never interacted with before. You find that you need to 
# write a script using the directory method to list all resources that 
# are available in that package.

# Aim
# Use a function which will take a package or module name and print out the 
# names of all the resources defined in the package or module using the directory method.

# Steps for Completion
# Define a function called resources_scanner that takes an argument package.
# Using the dir method create a variable to list all the resources that are available in that package.
# Inside the function, use a for statement to print and list each of the package’s resources.
# Run your script using the python3 main.py command in the terminal or by importing 
# and calling your method in the interactive python shell. The output should be as shown in 

# Snippet 8.37:

# >>> resources_scanner(string)
# Formatter
# Template
# _ChainMap
# _TemplateMetaclass
# __all__
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __spec__
# _re
# _string
# ascii_letters
# ascii_lowercase
# ascii_uppercase
# capwords
# digits
# hexdigits
# octdigits
# printable
# punctuation
# whitespace
# Snippet 8.37

# Write your function here
def resources_scanner(package):
    resources = dir(package)
    for resource in resources:
        print(resource)

if __name__ == '__main__':
    import string 
    resources_scanner(string)