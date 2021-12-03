def myfunc(val):
    print("Hello " + val)

myfunc("Python")
myfunc("Ruby")
myfunc("Java")

prime_numbers = [2, 3, 5, 7, 9, 11]
print(prime_numbers)

# remove all elements
prime_numbers.clear()

# Updated prime_numbers List
print('List after clear():', prime_numbers)


# Output: List after clear(): []

my_set = {2, 3, 5}
my_dict = {"name": "Ventsislav", "age": 24}
# my_file = open("file_name.txt")
squares = (n**2 for n in my_set)

things = ["second"]
things.insert(0, "first")
print(things)