# Adding Attributes to a Class

# Aim
# In this exercise, we will add attributes to a Person class.

# Steps for Completion
# First, create the Person class with a name attribute and instantiate an 
# object without passing any arguments as shown in Snippet 7.14:
# In [1]: class Person: 
#    ...:     def __init__(self, name): 
#    ...:         self.name = name 
#    ...:                                                                                                                                                                     

# In [2]: person1 = Person()                                                                                                                                                  
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-2-c5f82bb2701d> in <module>
# ----> 1 person1 = Person()

# TypeError: __init__() missing 1 required positional argument: 'name'
# Snippet 7.14

# Python throws us an error since we need to pass in a name argument when instantiating 
# a Person object. This argument is passed to the __init__ method when the object is 
# being instantiated.

# Instantiate a Person object, passing an argument for name as shown in Snippet 7.15:
# In [3]: person1 = Person("Bon Clay") 
# Snippet 7.15

# Now try to access the attribute from our instance as shown in Snippet 7.16:
# In [4]: person1.name                                                                                                                                                        
# Out[4]: 'Bon Clay'
# Snippet 7.16

# Redefine the Person class so that it is defining more attributes that instances 
# should be initialized with, for example, name, age, and height in centimeters as shown in 
# Snippet 7.17:
# In [5]: class Person: 
#    ...:     def __init__(self, name, age, height_in_cm): 
#    ...:         self.name = name 
#    ...:         self.age = age 
#    ...:         self.height_in_cm = height_in_cm 
#    ...:  
# Snippet 7.17

# Now, when instantiating a Person object, we'll need to pass in the three 
# arguments: name, age, and height_in_cm. Pass in the three values, as shown in 

# Snippet 7.18:
# In [6]: person1 = Person("Cubert", 62, 180)                                                                                                                                 
# In [7]: print(person1.name, person1.age, person1.height_in_cm)                                                                                                              
# Cubert 62 180
# Snippet 7.18

# Practive on the Terminal

# Python 3.7.4 (default, Sep  3 2019, 20:41:02) 
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.


class Person: 
    def __init__(self, name): 
        self.name = name 

# If you try to instance a class without the parameters, the compiler will trow a error
# person1 = Person()

person1 = Person("Bon Clay") 
print(person1.name)

class Person: 
    def __init__(self, name, age, height_in_cm): 
        self.name = name 
        self.age = age 
        self.height_in_cm = height_in_cm 

person1 = Person("Cubert", 62, 180)

print(person1.name, person1.age, person1.height_in_cm)