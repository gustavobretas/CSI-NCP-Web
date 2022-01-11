# Arranging and Presenting Data Using Dictionaries

# Scenario

# Given a word, write a function that will output a dictionary 
# that will give each character of the word and its frequency.

# Aim

# Due to its key-value pair format, dictionaries can be used to 
# present some forms of structured data in an easily readable way. 
# This challenge will help you write code to present frequency data 
# for characters in strings.

# Dictionaries are very good data structures for organizing data in a 
# readable format. Your aim is to write a function called word_counter, 
# which will take in a line of text and output a dictionary with each 
# letter as a key, the value being the frequency of appearance of the letter.

# Here are some hints to help you out:

# • Treat different uppercase and lowercase letters separately. 
# For example, M and m should have different counts.

# • Drop empty spaces.

# • Assume that sentences will not have any special characters.

# Steps for Completion
# Define the function word_counter and have it take a string argument.

# Iterate through the string and count the occurrences of each character.

# Output each character as a key in the output dictionary, with the frequency as the value.

# At the end of your script, call the word_counter function as shown in 

# Snippet 6.46, pass it the string "Mississippi" and print it to the console. 
# Here is an example:
# print(word_counter("Mississippi"))
# Snippet 6.46

# Run the script using python3 main.py, the output should look like 

# Figure 6.1:
# workspace $ python3 main.py
# {'M': 1, 'i': 4, 's': 4, 'p': 2}
# Figure 6.1

# Write your code here
def word_counter(text):
    counter = {}
    for char in text:
        if char != ' ':
            counter[char] = text.count(char)
    return counter

print(word_counter("Mississippi"))
print(word_counter("This is a test"))
