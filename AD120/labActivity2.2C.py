# Scenario

# You want to write a Python script that takes a 
# string and counts the occurrence of a specified word.

# Aim

# Write a script that counts and displays the number of 
# occurrences of a specified word in a given excerpt. 
# The script should request two input values from the user, 
# that is, the excerpt and the word to search for. You can 
# assume that the word will not occur as a substring in other words.

# Steps for Completion

# 1. Go to your main.py file.

# 2. Take in the user input for the sentence and the substring.

# 3. Next, sanitize and format the input by removing the whitespace 
# and converting it to lowercase.

# 4. Count the occurrences of the substring.

# 5. Print the results.

# 6. Run the script by using the python3 main.py command

# The output should look like Figure 2.11 shown below:

# workspace $ python3 main.py
# Sentence: You cannot end a sentence with because because because is a conjunction.
# Word to look for in sentence: because
# There are 3 occurrences of 'because' in the sentence
# workspace $ python3 main.py
# Sentence: That that is is that that is not is not. Is that it? It is.
# Word to look for in sentence: that
# There are 5 occurrences of 'that' in the sentence
# workspace $ python3 main.py
# Sentence: She said said is said said but I said no said is said said.
# Word to look for in sentence: said
# There are 8 occurrences of 'said' in the sentence
# workspace $ 

# Write your code here
excerpt = input("Sentence: ")
word = input("Word to look for in sentence: ")
print("There are", excerpt.lower().count(word), "occurrences of '" + word + "' in the sentence")
