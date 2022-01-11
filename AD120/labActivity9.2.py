# Identifying Error Scenarios

# Scenario
# You are testing code to determine types of errors. During programming, 
# errors often occur. But how can we anticipate when something will cause 
# an error? You can anticipate errors by thoroughly understanding error 
# scenarios and causes.

# Aim
# In this activity, we will create error scenarios. Let’s write some code 
# that will cause a KeyError and an AttributeError.

# Steps for Completion
# Go to your main.py file.

# Define a function createError to first generate a KeyError and then an AttributeError.

# In order to generate both errors, you will need to generate only one error at a time.

# Grading
# Complete each task listed below. Each task contains automated checks which 
# are used to calculate your grade. When you have completed each task by clicking 
# the checkbox, open the task list panel on the left navigation bar and click 
# the "Submit" button.

# To generate a KeyError:

# Create the dictionary shown in Snippet 9.29:

# dinning = dict (
#  name = "Johnny's Restaurant",
#  location = "Times Square"
# )
# Snippet 9.29

# Write a print statement that uses a key that’s not defined in this dictionary.

# Running the script with python3 main.py should result in only one console 
# error similar to the example below:

# KeyError: 'address'
# Task

# Modify main.py to create a KeyError.

# To generate an AttributeError:

# Import the string module.

# Use an attribute that’s not defined in the string module.

# Running the script with python3 main.py should result in only one console 
# error similar to the example below:

# Use the function return to create an error
def createError():
    # Task 1
    # Write your code here
    dinning = dict (
        name = "Johnny's Restaurant",
        location = "Times Square"
    )
    print(f"I went to eat at {dinning['name']} yesterday in {dinning['address']}.")
    # Task 2
    # Write you import modules here
    import string
    letters = string.asciiletters

    return

# Use this code to test your function
if __name__ == '__main__':
    createError()
