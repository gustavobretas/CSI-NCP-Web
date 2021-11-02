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