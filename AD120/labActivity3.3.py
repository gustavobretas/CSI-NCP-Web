# The for Loop and the range Function

# Aim
# The aim of this activity is to create a password authentication feature using a while loop.

# You have been asked to add a simple password authentication feature for a prototype 
# that your team is setting up. One of your team members has advised the use of a while loop.

# Steps for Completion
# Create a script called main.py.

# Define input("Enter your name: ") as the name, Pas$Word as the password, and the Boolean variable first.

# Initiate the while loop and for the password ask for the user's input.

# Validate the password. If the password is correct, print "Welcome back, name". 
# If the validation fails return an error and print the message "Incorrect password, try again...".

# Run the script in the terminal using the command python3 main.py.

# The output should be as shown in Snippet 3.32:

# python3 main.py
# Enter your name: Josh
# Enter your password: Pas$Word
# Welcome back, Josh
 
# python3 main.py
# Enter your name: Josh
# Enter your password: none
# Incorrect password, try again...
# Enter your password:
# Snippet 3.32

# Write your code here
name = input("Enter your name: ")
loop = True
while loop == True:
    password = input('Enter your password: ')
    if password == 'Pas$Word':
        loop = False
        print('Welcome back,', name)
    else:
        print('Incorrect password, try again...')

