# Aim

# Write a Python script that breaks down all the words 
# of a sentence and prints each word on its own line. 
# The goal of this exercise is to get familiar with 
# escape sequences:

# Steps for Completion
# 1. Go to your main.py file and in the first line, request the 
# sentences to split from the user:
# sentence = input("Sentence: ")
# 2. Next, replace all of the spaces in the sentence with 
# newline characters:
# sentence = sentence.replace(" ", "\n")
# 3. Finally, print out the sentence. Each word should appear 
# on a new line as shown in Snippet 2.60:

# sentence = input("Sentence: ")
# sentence = sentence.replace(" ", "\n")
# print(sentence, "\a")
# Snippet 2.60

# You can run the script by using the python3 main.py command. 
# An example is shown in Figure 2.10 below:
# workspace $ python3 main.py
# Sentence: The quick brown fox jumps over the lazy dog
# The
# quick
# brown
# fox
# jumps
# over
# the
# lazy
# dog 

# Write your code here
sentence = input("Sentence: ")
sentence = sentence.replace(" ", "\n")
print(sentence, "\a")

