# Defining a Class and Objects

# Aim
# Suppose you are a backend developer for a tech news platform. You have been 
# asked to design a templating system for their news articles. To do this, you will 
# need to run some proof of concepts.

# Steps for Completion
# Define the TabletComputer class in the main.py file so that the code in 

# Snippet 7.19 runs without error:
# # Write your TabletComputer class here
 
# uPad = TabletComputer(12.9, "1TB", "uPadOS 13.5.1")
# rootProX = TabletComputer(13.0, "512GB", "Glass 10 Home")
 
# print(f"The new uPad has a {uPad.screen_size}"
#     f" inch display. A maximum {uPad.storage} of storage and runs on"
#     f" the latest version of {uPad.os}. Its biggest competitor is"
#     f" the Root Pro X which holds a similar {rootProX.screen_size}"
#     f" inch display, with a maximum storage capacity of {rootProX.storage} and runs {rootProX.os}."
#       )
# Snippet 7.19

# Define the __init__ function within the TabletComputer class with the necessary 
# parameters to set up the member variables.

# You will need to set the following member variables:

# screen_size
# storage
# os
# After defining the class, running the preceding code should yield the output shown in Figure 7.1:

# https://cdn.filestackcontent.com/0rPgNyeXStaB4a44JGMI

# workspace $ python3 main.py
# The new uPad has a 12.9 inch display. A maximum 1TB of storage and runs on the 
# latest version of uPadOS 13.5.1. Its biggest competitor is the Root Pro X which 
# holds a similar 13.0 inch display, with a maximum storage capacity of 512GB and 
# runs Glass 10 Home.
# workspace $ 

# Figure 7.1

# Write your TabletComputer class here

class TabletComputer:
    def __init__(self, screen_size, storage, os):
        self.screen_size = screen_size
        self.storage = storage
        self.os = os

uPad = TabletComputer(12.9, "1TB", "uPadOS 13.5.1")
rootProX = TabletComputer(13.0, "512GB", "Glass 10 Home")

print(f"The new uPad has a {uPad.screen_size} "
	f"inch display. A maximum {uPad.storage} of storage and runs on "
    f"the latest version of {uPad.os}. Its biggest competitor is "
    f"the Root Pro X which holds a similar {rootProX.screen_size} "
    f"inch display, with a maximum storage capacity of {rootProX.storage} and runs {rootProX.os}.")
