# Creating Unions of Elements in a Collection

# Scenario
# Given two lists, create a function that returns a list 
# of all of the elements in both lists, with no duplicates.

# Aim
# The aim of this activity is to implement an algorithm that 
# returns the union of elements in a collection.

# Although working with sets is quick and easy in Python, sometimes 
# we might want to find the union between two lists. Create a function 
# called unite_lists, which uses a loop to go through both lists and 
# return common elements. Do not use the built-in set function.

# Steps for Completion
# Define a function named unite_lists.

# Using a for statement, iterate through the two lists, while finding 
# the common elements in both lists without duplicates.

# Snippet 6.109 shows an example output:

# >>> unite_lists([2,4,6,8],[3,6,9,12])

# [2, 4, 6, 8, 3, 9, 12]
# Snippet 6.109

# Write your code here
def unite_lists(list1, list2):
    unitedList = []
    for element in list1 + list2:
        if element not in unitedList:
            unitedList.append(element)
    return unitedList
    
# Test your code here
if __name__ == '__main__':
    print(unite_lists([2,4,6,8],[3,6,9,12]))
