# Nested Loops

# Aim

# Write a simple nested loop example that sums the even and odd 
# numbers between 5 and 15 and prints out the computation.

# Steps for Completion

# 1 Write a for loop with a range function for even numbers.

# 2 Write a for loop with a range function for odd numbers.
 
# 3 Use a variable called calc to calculate the sum of even and odd numbers.

# 4 Print the computation of each even number plus the odd number equal to calc to the terminal.

# The output will be as shown in 
# Snippet 3.58:
# 6 + 5 = 11
# 6 + 7 = 13
# 6 + 9 = 15
# 6 + 11 = 17
# 6 + 13 = 19
# 8 + 5 = 13
# 8 + 7 = 15
# 8 + 9 = 17
# 8 + 11 = 19
# 8 + 13 = 21
# 10 + 5 = 15
# 10 + 7 = 17
# 10 + 9 = 19
# 10 + 11 = 21
# 10 + 13 = 23
# 12 + 5 = 17
# 12 + 7 = 19
# 12 + 9 = 21
# 12 + 11 = 23
# 12 + 13 = 25
# 14 + 5 = 19
# 14 + 7 = 21
# 14 + 9 = 23
# 14 + 11 = 25
# 14 + 13 = 27
# Snippet 3.58

# Write your code here
for i in range(6, 15, 2):
    for j in range(5, 15, 2):
        print(i, '+', j, '=', i + j)
