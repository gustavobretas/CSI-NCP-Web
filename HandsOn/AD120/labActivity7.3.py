# Defining Methods in a Class

# Scenario
# You are part of a race team building a program to help children learn math in a fun way. 
# Currently, you're building a module on shapes, more specifically, calculating the 
# circumference and area of circles.

# Aim
# The formula for calculating the circumference of a circle is 2*π*r. The formula 
# for calculating the area of a circle is π*r*r.

# Write a Python class named Wheel, constructed by a radius and two methods, which will 
# calculate the perimeter (circumference) and the surface area of a wheel (circle).

# The script should ask for the user's input for the radius, create a Wheel object, and 
# print out its surface area and perimeter. It should ask for the user's input again 
# after it prints the surface area and perimeter each time. You should use the math modules 
# and set the pi constant as your value for pi. Our aim here is to practice defining 
# methods in a class.

# Steps for Completion
# Open the file named main.py.

# Define the Wheel class and the Wheel constructor method.

# Create the wheel_area calculation method, which returns the surface area of the wheel.

# Create the wheel_perimeter calculation method, which returns the perimeter of the wheel.

# Create the swap_radius method, which sets new_radius as the radius of the wheel 
# when requested from user input.

# After the class definition, add the code that requests for user input for the 
# radius of the wheel.

# Create a __main__ and add a while loop so that the request for user input runs 
# multiple times. In the while loop, we'll request the user input, change the Wheel 
# object's radius using the swap_radius method, and then print out the surface area 
# and perimeter of the wheel.

# Make sure that your program terminates properly when the user indicates they would like to quit.

# You can run the script by using python3 main.py command. The script will ask for 
# user input, calculate the surface area and perimeter, print that out, and ask for 
# your input again. The output should look like 

# Figure 7.2:

# https://cdn.filestackcontent.com/1XtinpTTKmhyc6VzvAcc
# workspace $ python3 main.py
# Radius of wheel: 7
# Surface area of wheel: 153.93804002589985
# Perimeter of wheel: 43.982297150257104
# More wheels? Y/N y
# Radius of wheel: 3
# Surface area of wheel: 28.274333882308138
# Perimeter of wheel: 18.84955592153876
# More wheels? Y/N y
# Radius of wheel: 10
# Surface area of wheel: 314.1592653589793
# Perimeter of wheel: 62.83185307179586
# More wheels? Y/N n
# workspace $ 

# Figure 7.2

# Write your code here
import math

# Write your Wheel class here
class Wheel:
    radius = 0
    def __init__(self, radius):
        self.radius = radius

    def swap_radius(self, new_radius):
        self.radius = new_radius
        return self.radius

    def wheel_area(self):
        area = math.pi * self.radius * self.radius
        return area

    def wheel_perimeter(self):
        circle = 2 * math.pi * self.radius
        return circle
        

# Use this to test your code
if __name__ == "__main__":
    wheel = Wheel(7)
    morewheels = True
    while morewheels:
        radius = float(input("Radius of wheel: "))
        wheel.swap_radius(radius)
        print("Surface area of wheel:", wheel.wheel_area())
        print("Perimeter of wheel:", wheel.wheel_perimeter())
        yn = input('More wheels? Y/N ')
        morewheels = yn == 'y' or yn == 'Y'
