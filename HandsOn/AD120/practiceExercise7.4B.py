# Implementing a Counter for Instances of a Class

# Aim
# Our aim here is to thoroughly understand class attributes. In this exercise, 
# we're going to create a counter that will be incremented each time a new 
# WebBrowser object is instantiated:

# Steps for Completion
# Add the class attribute number_of_web_browsers, which will serve as the counter 
# and will start at 0 as shown in Snippet 7.41:

# class WebBrowser:
#     number_of_web_browsers = 0
#     connected = True
#     def __init__(self, page):
#         self.history = [page]
#         self.current_page = page
#         self.is_incognito = False
# Snippet 7.41

# Modify the constructor to increment the counter each time a new instance is created 
# by adding the line WebBrowser.number_of_web_browsers += 1 as shown in Snippet 7.42. 
# This increments the number_of_web_browsers attribute of our class by 1 and will be 
# called each time a new instance is initialized:
# class WebBrowser:
#     number_of_web_browsers = 0
#     connected = True
#     def __init__(self, page):
#         self.history = [page]
#         self.current_page = page
#         self.is_incognito = False
#         WebBrowser.number_of_web_browsers += 1
# Snippet 7.42

# Let's test it out:

# First, check that the number_of_web_browsers counter is at 0 as shown in Snippet 7.43:
# >>> from main import WebBrowser
# >>> WebBrowser.number_of_web_browsers
# 0
# >>>
# Snippet 7.43

# Next, instantiate a new object and check the counter as shown in Snippet 7.44:
# >>> opera = WebBrowser("opera.com")
# >>> WebBrowser.number_of_web_browsers
# 1
# >>>
# Snippet 7.44

# The counter increments with every other instance we create. Check this, as shown in Snippet 7.45:
# >>> edge = WebBrowser("microsoft.com")
# >>> WebBrowser.number_of_web_browsers
# 2
# >>>
# Snippet 7.45

# Besides the use cases we've seen, class attributes should be used when you have variables 
# that are common to all instances, such as constants for the class.

# Your code here
class WebBrowser:
    number_of_web_browsers = 0
    connected = True
    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
        WebBrowser.number_of_web_browsers += 1

print(WebBrowser.number_of_web_browsers)

opera = WebBrowser("opera.com")
print(WebBrowser.number_of_web_browsers)

edge = WebBrowser("microsoft.com")
print(WebBrowser.number_of_web_browsers)