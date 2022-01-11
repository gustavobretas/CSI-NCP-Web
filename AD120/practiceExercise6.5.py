# Adding Data to a Dictionary

# Aim
# In this exercise, we will practice set operations.

# Steps for Completion
# Go to the main.py file.
# Create two sets as shown in Snippet 6.120:

# l = {"lion", "tiger", "giraffe", "frog"}
# w = {"frog", "fish", "octopus"}
# Snippet 6.120

# Find the union of the two sets as shown in Snippet 6.121:

# l.union(w)
# Snippet 6.121

# The output, when printed, is as shown in Snippet 6.122:

# {'lion', 'tiger', 'giraffe', 'frog', 'fish', 'octopus'}
# Snippet 6.122

# Find the intersection of the two sets as shown in Snippet 6.123:
# l.intersection(w)
# Snippet 6.123
# The output, when printed, is as shown in Snippet 6.124:

# {'frog'}
# Snippet 6.124

# Find the difference between the sets as shown in Snippet 6.125;
# l - w
# Snippet 6.125
# The output, when printed, is as shown in Snippet 6.126:

# {'lion', 'tiger', 'giraffe'}
# Snippet 6.126

# Find the symmetric difference of the sets as shown in Snippet 6.127:
# l.symmetric_difference(w)
# Snippet 6.127
# The output, when printed, is as shown in Snippet 6.128:

# {'lion', 'tiger', 'giraffe', 'fish', 'octopus'}
# Snippet 6.128

# Write your code here
l = {"lion", "tiger", "giraffe", "frog"}
w = {"frog", "fish", "octopus"}

print(l.union(w))
print(l.intersection(w))

print(l - w)

print(l.symmetric_difference(w))