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

dictionary_masher = {
    "name": "Amos",
    "age": 100
}

print(dictionary_masher)

a = {1,2,3,4,5,6}
b = {1,2,3,7,8,9,10}

print(a.union(b))
print(a.intersection(b))

class Person:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Hello! " + self.name)

p = Person("Python")
p.speak()

class Car:
    def __init__(self):
        self._speed = 300
        self._color = "black"

car = Car()
car._speed = 400
print(car._speed)

v = [(0,0), (0,1),(1,0),(1,1)]
index_list = [0,1,2,1,2,3]

v_list = [i for i in range(2, len(index_list), 3)]
indices = index_list
triangle_list = [(v[indices[i-2]], v[indices[i-1]]) for i in v_list]

print(triangle_list)

x_axis = [0,2,4,8]
y_axis = [10,20,30,40]

graph_data = [(x,y) for x in x_axis for y in y_axis]
print(graph_data)

person = {
    "name": "Rich Brown",
    "age": 56
}

print(person["gender"])