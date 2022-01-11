# Aim
# In this exercise, we will practice data operations on a set.

# Steps for Completion
# Go to the main.py file.
# Create a set as shown in Snippet 6.95:
# v = set({"car", "bus", "train"})
# print(v)
# Snippet 6.95
# The output is as shown in Snippet 6.96:

# ("car", "bus", "train")
# Snippet 6.96

# Add bicycle to the set as shown in 

# Snippet 6.97:
# v.add("bicycle")
# print(v)
# Snippet 6.97

# The output is as shown in 

# Snippet 6.98:

# ("car", "bus", "train", "bicycle")
# Snippet 6.98

# Read data from the set using iterables as shown in 

# Snippet 6.99:
# for veh in v:
#      print(veh)
# Snippet 6.99
# The output is as shown in 

# Snippet 6.100:

# car
# bus
# train
# bicycle
# Snippet 6.100

# Remove one item from the set using the pop() function as shown in 

# Snippet 6.101:
# print(v.pop())
# Snippet 6.101

# The output is as shown in 

# Snippet 6.102:

# 'bus'
# Snippet 6.102

# Remove the car vehicle from the set as shown in 

# Snippet 6.103:
# v.remove("car")
# print(v)
# Snippet 6.103

# The output is as shown in 

# Snippet 6.104:

# {'bicycle', 'train'}
# Snippet 6.104

# Clear the set using the clear() method as shown in 

# Snippet 6.105:
# v.clear()
# print(v)
# Snippet 6.105

# The output is as shown in 

# Snippet 6.106:

# {}

# Write your code here
v = set({"car", "bus", "train"})
print(v)

v.add("bicycle")
print(v)

for veh in v:
     print(veh)

print(v.pop())
print(v)

v.remove("train")
print(v)

v.clear()

print(v)