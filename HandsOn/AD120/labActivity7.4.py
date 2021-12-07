# Creating Class Attributes

# Scenario
# Suppose you are designing a piece of software for a packaging company. 
# A part of the software involves an items capacity limit mechanism to prevent 
# a package from being shipped when it's filled past its capacity.

# Aim
# Define a class called Package, which will have a maximum item capacity of 6.

# The package should be initialized with the number of items.
# If the number of items exceeds the capacity limit during initialization, it should 
# print out a message indicating that the limit has been exceeded and only initialize 
# how many items should be removed from the package.
# Otherwise, if the number of items does not exceed the limit, it should print out a 
# message that includes how many items are in the package.
# Our aim here is to practice creating class attributes.

# Steps for Completion
# Go to you main.py file.

# In the space provided, declare the Package class by adding an items limit class attribute.

# Add the initializer, which will check whether the item limit will be exceeded, and print 
# a message indicating how many items must be removed.

# If the items limit has not been exceeded, print out the number of items in the package.

# Finally, create a while loop that requests the user to input the number of items and 
# then asks if we'd like to continue.

# Create a few instances of the class declaration to test your implementation, 

# Snippet 7.46 shows an example:

# package1 = Package(6)
# print("There are", package1.items, "items in the package being shipped out.")
# package2 = Package(10)
# print("There are", package2.items, "items in the package being shipped out.")
# Snippet 7.46

# Run the script by running the python3 main.py command in the terminal. 
# The output should look similar to Figure 7.3:

# workspace $
# How many items are in the package?: 4
# There are 4 items in the package being shipped out.
# Ship more packages? Y/N y
# How many items are in the package?: 6
# There are 6 items in the package being shipped out.
# Ship more packages? Y/N y
# How many items are in the package?: 10
# The maximum item limit has been exceeded. 4 items must be removed from the package.
# Ship more packages? Y/N n
# workspace $

# Figure 7.3

# Write your Package class here
class Package:
    itemsLimit = 6
    items = 0
    def __init__(Self, initialItems):
        Package.items = initialItems
        if Package.items > Package.itemsLimit:
            print('The maximum item limit has been exceeded.', Package.items - Package.itemsLimit, 'items must be removed from the package.')
        else:
            print("There are", Package.items, "items in the package being shipped out.")


# This is to test your code
if __name__ == '__main__':
    morepackages = True
    while morepackages:
        items = int(input("How many items are in the package?: "))
        package = Package(items)
        yn = input('Ship more packages? Y/N ')
        morepackages = yn == 'y' or yn == 'Y'
