# Practicing Multiple Inheritance

# Scenario
# It's the year 2017. You're working for an electronics company and have been tasked 
# with modeling out the software for a cutting-edge tablet that will have a built-in 
# face recognition front camera: a biometric tablet.

# Aim
# Create a class called TabletCamera and a class called Facial_recognition that will be 
# the base classes of a derived class called BioTablet.

# Steps for Completion
# Create a TabletCamera class that will be initialized with a pixels attribute.

# Create a Facial_recognition class with a scan_face method that prints the message, Scanning Face...

# Create a BioTablet class that inherits from both the TabletCamera and Facial_recognition classes.

# At the bottom of the script initialize an instance of the BioTablet class and pass it the 
# value "12MP". Then we call the scan_face method and also print out the pixels attribute.

# Run the script with python3 main.py command and we should have an output that looks like 

# Snippet 7.91:

# Scanning Face...
# 12MP

# Snippet 7.91

# Write the TabletCamera class here 
class TabletCamera:
    def __init__(self, pixels):
        self.pixels = pixels

# Write the Facial_recognition class here
class Facial_recognition:
    def scan_face(self):
        print("Scanning Face...")

# Write the BioTablet class here
class BioTablet(TabletCamera, Facial_recognition):
    pass

# Write an instance of the BioTablet class
if __name__ == '__main__':
    biotablet = BioTablet("12MP")
# Call the scan_face method from the instance
    biotablet.scan_face()
# Print the pixels from the instance
    print(biotablet.pixels)
