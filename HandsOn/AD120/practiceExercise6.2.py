# Adding Data to a Dictionary

# Aim

# Consider the text frequency scenario that we considered in 
# Practice Exercise 6.1. We’ll now perform further operations on the 
# dictionary we created.

# Steps for Completion
# Go to the main.py file.
# Create the dictionary freqDict as shown in 

# Snippet 6.62:
# freqDict = {"hi": 45, "this": 35, "the": 28}
# Snippet 6.62

# Update the occurrence of the word the to 40 using the update() command as shown in 

# Snippet 6.63:
# freqDict.update({"the":40})
# Snippet 6.63

# Print the dictionary once again to verify it was updated as shown in 

# Snippet 6.64:
# print(freqDict)
# Snippet 6.64

# The output is as shown in Snippet 6.65:

# {'hi': 45, 'this': 35, 'the': 40}
# Snippet 6.65

# Create a copy of the dictionary using the copy() command as shown in 

# Snippet 6.66:
# copyFreqDict = freqDict.copy()
# print(copyFreqDict)
# Snippet 6.66
# The output is as shown in Snippet 6.67:

# {'hi': 45, 'the': 40, 'this': 35}
# Snippet 6.67

# Remove a random item from the dictionary as shown in 

# Snippet 6.68:
# print(copyFreqDict.popitem())
# Snippet 6.68
# The output will pop one of the items as shown in 

# Snippet 6.69:
# {'hi', 45}
# Snippet 6.69

# Add the word data into the dictionary only if the word does not exist 
# using the setdefault() function as shown in 

# Snippet 6.70:
# newFreqDict = copyFreqDict.setdefault("data", "21")
# print(newFreqDict)
# Snippet 6.70

# The value in the second argument will be output as shown in 

# Snippet 6.71:
# '21'
# Snippet 6.71

# Remove the word this and its frequency from the dictionary 
# using the pop() command as shown in 

# Snippet 6.72:
# count = freqDict.pop("this")
# print(count)
# Snippet 6.72


# The output is as shown in Snippet 6.73:
# 35
# Snippet 6.73

# Suppose the data in the dictionary has become incorrect and you have to 
# empty the entire dictionary. You can do so using the clear() command as shown in 

# Snippet 6.74:
# freqDict.clear()
# print(freqDict)
# Snippet 6.74

# The output is as shown in Snippet 6.75:
# {}
# Snippet 6.75

# Create a dictionary using fromkeys() function as shown in 

# Snippet 6.76:
# keys = {'d', 'i', 'c', 't'}
# value = [1]
# newDict = dict.fromkeys(keys, value)
# print(newDict)
# Snippet 6.76

# The output will be as shown in Snippet 6.77:
# {'d': [1], 'i': [1], 'c': [1]. 't': [1]}
# Snippet 6.77

# Write your code here
freqDict = {"hi": 45, "this": 35, "the": 28}
freqDict.update({"the":40})
print(freqDict)
copyFreqDict = freqDict.copy()
print(copyFreqDict)
print(copyFreqDict.popitem())
newFreqDict = copyFreqDict.setdefault("data", "21")
print(newFreqDict)
count = freqDict.pop("this")
print(count)
freqDict.clear()
print(freqDict)
keys = {'d', 'i', 'c', 't'}
value = [1]
newDict = dict.fromkeys(keys, value)
print(newDict)
