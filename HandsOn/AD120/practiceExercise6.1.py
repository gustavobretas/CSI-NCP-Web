# Adding Data to a Dictionary

# Aim

# Suppose you have chunks of text data and you want to save the words 
# in a dictionary with their frequency of occurrence.

# Steps for Completion
# Go to your main.py file.
# Create a dictionary as shown in 

# Snippet 6.24:
# In [1]: freqDict = {"hi":45, "this":35, "the":28}    
# Snippet 6.24

# Print the values in the dictionary using the command shown in 

# Snippet 6.25:
# In [2]: print(freqDict) 
# Snippet 6.25

# The output will be as shown in 

# Snippet 6.26:
# {'this': 35, 'hi': 45, 'the': 28}
# Snippet 6.26

# Add another word and to the dictionary as shown in 

# Snippet 6.27:
# In [3]: freqDict['and'] = 20
# Snippet 6.27

# Print the values in the dictionary using the command shown in 

# Snippet 6.28:
# In [4]: print(freqDict)  
# Snippet 6.28

# The output is as shown in Snippet 6.29:

# {'hi': 45, 'this': 35, 'the': 28, 'and': 20}
# Snippet 6.29

# Read the frequency of the word this using the get() function. 
# Print the result as shown in 

# Snippet 6.30:
# In [5]: print(freqDict.get('this')) 
# Snippet 6.30

# The output is as shown in 

# Snippet 6.31:
# 35
# Snippet 6.31

# Read the frequency of word from. Note that the word is not available in dictionary. 
# Print the result as shown in 

# Snippet 6.32:
# In [6]: print(freqDict.get('from'))
# Spippet 6.32

# The output is as shown in 

# Snippet 6.33:
# None
# Snippet 6.33

# Specify the message to be displayed in case the word passed through the get() 
# function is not in the dictionary, as shown in 

# Snippet 6.34:
# In [7]: print(freqDict.get('from', 'Word does not exist in the dictionary')) 
# Snippet 6.34

# The output is as shown in 

# Snippet 6.35:
# Word does not exist in the dictionary
# Snippet 6.35

# Print the words in the dictionary using the keys() method as shown in 

# Snippet 6.36:
# In [8]: for item in freqDict.keys(): 
# ...:      print(item) 
# Snippet 6.36

# The output is as shown in 

# Snippet 6.37:
# hi
# this
# the
# and
# Snippet 6.37

# Print the frequency of the words using the values() method as shown in 

# ippet 6.38:
# In [9]: for item in freqDict.values(): 
# ...:     print(item) 
# Snippet 6.38

# The output is as shown in Snippet 6.39:
# 45
# 35
# 28
# 20
# Snippet 6.39

# Print the words with the frequency of their occurrence together as shown in 

# Snippet 6.40:
# In [10]: for key, value in freqDict.items(): 
# ...:     print(key, value) 
# Snippet 6.40


# The output is as shown in Snippet 6.41:
# ('hi', 45)
# ('this', 35)
# ('the', 28)
# ('and', 20)
# Snippet 6.41

# Check if a word exists in the dictionary using the in keyword. 

# Snippet 6.42 shows some examples:
# In [11]: print("hi" in freqDict) 
# ...: print("hello" in freqDict)   
# Snippet 6.42

# The output of the statements above is shown in 

# Snippet 6.43:
# True
# False
# Snippet 6.43

# Write your code here --> Run the code on Interpreter, line by line

freqDict = {"hi":45, "this":35, "the":28} 
print(freqDict)  
freqDict['and'] = 20  
print(freqDict)  
print(freqDict.get('this'))  
print(freqDict.get('from'))  
print(freqDict.get('from', 'Word does not exist in the dictionary'))

for item in freqDict.keys():
    print(item)

for item in freqDict.values():
    print(item) 

for key, value in freqDict.items(): 
    print(key, value) 

print("hi" in freqDict)
print("hello" in freqDict)
print("hello" not in freqDict)