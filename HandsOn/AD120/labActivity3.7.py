# The for Loop and the range Function

# Aim

# Using a for loop and a range function, you have been asked to 
# find the even numbers between 5 and 55 and then find their sum.

# Steps for Completion

# 1 Define a counter for the sum named total_sum.

# 2 Define a for loop with an even range for numbers between 5 and 55.

# 3 Add each looped number to the sum.

# 4 Outside the loop, print out total_sum.

# The output should be as shown in 
# Snippet 3.50:
# 750
# Snippet 3.50

# Write your code here
total_sum = 0
for i in range(5, 55):
    if i % 2 == 0:
        total_sum += i
print(total_sum)
