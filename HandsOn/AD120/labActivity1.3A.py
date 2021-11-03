# Scenario
# You are creating a simple Python script that takes a 
# distance and a completion time and outputs the speed in 
# knots, miles per hour, and feet per second.

# Aim
# Using variables write a script that defines a distance 
# of 60 miles and a completion time of 3 hours. The output should 
# show a completion speed in miles per hour, knots, and feet per second.

# Here are some hints:

# The formula for calculating speed is distance/time = speed.
# To convert miles to knots, divide the miles by 1.15078.
# To convert miles to feet, multiply the miles by 5280.
# To convert hours to seconds, multiply hours by 3600.
# The output should resemble Figure 1.8 shown below.
# Steps for Completion
# Go to your main.py file.

# On the first two lines, declare two variables for the distance 
# in miles and time in hours and assign the values 60 and 3, respectively.

# In the next two lines, calculate the distance in knots and 
# distance in feet based on the distance in miles.

# Then, calculate the time in seconds based on the time in hours.

# Next, calculate the speed in knots, speed in miles per hour, 
# and speed in feet per second.

# Finally, add print statements to print out the results.

# In your terminal, run the script by using the python3 main.py command.

# The output should be like Figure 1.8, shown below:
# The speed in Knots is: 17.37951650185092
# The speed in miles per hour is: 20.0
# The speed in feet per second is: 29.333333333333332

# Write your code here
distanceInMiles = 60
timeInHours = 3
distanceInKnots = distanceInMiles / 1.15078
distanceInFeet = distanceInMiles * 5280
timeInSeconds = timeInHours * 3600
speedInKnots = distanceInKnots / timeInHours
speedInMPH = distanceInMiles / timeInHours
speedInFtPerSecond = distanceInFeet / timeInSeconds
print("The speed in Knots is: " + str(speedInKnots))
print("The speed in miles per hour is: " + str(speedInMPH))
print("The speed in feet per second is: " + str(speedInFtPerSecond))