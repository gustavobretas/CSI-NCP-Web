Handling Errors

Scenario
You are completing some code, but you have an unhandled error. 
What do you do to make sure that the error doesn't stop your program prematurely?

Aim
In this activity, we will practice handling errors. The code in 

Snippet 9.53 throws an error.

The following code throws an error:

import random
 
print(random.randinteger(5,15))
Snippet 9.53

Identify and handle the error so that when it occurs, the message is printed to the terminal.

Steps for Completion
Go to your main.py file.

Take the code block from Snippet 9.53, and amend to it so that it catches the 
error, using a try… except block.

Within the try... except block make the exception look for an AttriubuteError 
and print Double check the attributes in your code and try again.