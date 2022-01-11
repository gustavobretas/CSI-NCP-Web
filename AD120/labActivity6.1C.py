# Combining Dictionaries

# Scenario

# You have two dictionaries that you need to process together. 
# Write a Python function to combine the contents.

# Aim
# Combine two dictionaries and return a single dictionary with non-duplicate keys.

# Steps for Completion
# Write a function called content_combiner that will take two dictionaries 
# and return a single dictionary with non-duplicate keys.

# The output should be as shown in 

# Snippet 6.47:
# {'gold': 'Yellow', 'karats': 24}
# Snippet 6.47

# Write your code here
def content_combiner(dict_a, dict_b):
    combined = dict_a
    for key, value in dict_b.items():
        if key not in dict_a:
            combined[key] = value
    return combined


# Test your function using the code below
if __name__ == '__main__':
    print(content_combiner({"gold": "Yellow"}, {"karats": 24}))
