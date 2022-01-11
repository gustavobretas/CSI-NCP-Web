# Using the List Methods

# Scenario
# Given the following challenges, use append(), extend(), pop(), and 
# insert()to change the contents of the lists.

# Aim
# The aim of this activity is to get acquainted with list 
# methods by utilizing various Python list methods.

# Using the ipython3 interactive shell, change the contents of this 
# list using the various available methods.

# Steps for Completion
# Suppose that we have the following list:

# Strawberry, Blueberry, Blackberry, Cranberry

# Define the list berries with the following elements shown in
# Snippet 5.11:
#    Strawberry, Blueberry, Blackberry, Cranberry
# Snippet 5.11

# Change the contents of this list using the various available methods:

# Note: Check your output by calling the list after each method

# Using the built-in append() method, add the value Raspberry to the list berries.

# Using the built-in extend() method, extend an empty fruits list from the berries 
# list that you created previously.

# Insert Mangoes into the fruits list at index 2 using the built-in method insert().

# Remove the element at index 1 from the fruits list using the built-in method pop() 
# and replace it with Apples, using the insert() built-in method.

# Finally, sort the elements in the fruits list by using the built-in method sort() 
# with keyword arguments. Set the key argument to None and the reverse argument to False.

# Write your code here --> Run the code on Interpreter, line by line
In [1]: berries = ["Strawberry", "Blueberry", "Blackberry", "Cranberry"]                                                

In [2]: berries.append("Raspberry")                                                                                     

In [3]: fruits = []                                                                                                     

In [4]: fruits.extend(berries)                                                                                          

In [5]: fruits.insert(2, "Mangoes")                                                                                     

In [6]: fruits.pop(1)                                                                                                   
Out[6]: 'Blueberry'

In [7]: fruits.insert(1, "Apples")                                                                                      

In [8]: fruits.sort(key = None, reverse = False)                                                                        

In [9]:  