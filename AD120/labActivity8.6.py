# Performing File Operations

# Aim
# Create a file and add data to it.

# Steps for Completion
# In your main.py file, use the with context manager or the open() 
# function to create a newfile.txt object.

# Write I enjoy learning to code in Python to the file.

# Run your script with python3 main.py, a file named newfile.txt should 
# be generated with the contents I enjoy learning to code in Python.

# Remember to close the file object when you are only using open().

# Write your code here
with open("newfile.txt", 'w') as file:
    file.write("I enjoy learning to code in Python")
