# Aim

# See how list references work:

# Steps for Completion
# Create a new list, as shown in Snippet
# >>> list_1 = [1, 2, 3]

# Then, assign a new variable, list_2, to list_1 using the command shown in Snippet
# >>> list_2 = list_1

# Any changes that we make to list_2 will be applied to list_1. Append 4 to list_2 and check 
# the contents of list_1 as shown in Snippet
# >>> list_2.append(4)
# >>> list_1
# [1, 2, 3, 4]

# Any changes that we make to list_1 will be applied to list_2. Insert the value a at 
# index 0 of list_1, and check the contents of list_2 as shown in Snippet 
# >>> list_1[0] = "a"
# >>> list_2
# ['a', 2, 3, 4]
# >>>

# This is because both variables reference the same object.

# Write your code here
list_1 = [1, 2, 3]
list_2 = list_1
list_2.append(4)
list_1[0] = "a"
print(list_2)