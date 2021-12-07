# Creating Class Methods and Using Information Hiding

# Scenario
# Suppose you work for an electronics company that has a new MoviePlayer device that 
# it wants to release to the market. The software for this device needs to support 
# over-the-air updates that enables users to watch their favorite movies painlessly.

# Aim
# Create a class that represents a portable movie player, MoviePlayer. The MoviePlayer 
# class should have a play method, which sets the first movie from the list of movies 
# as currently playing. The list of movies should be a private attribute. Additionally, 
# it should have a firmware version attribute and an update firmware class method that 
# updates the firmware version.

# Steps for Completion
# Go to your main.py file.

# Define the MoviePlayer class by adding the firmware_version class attribute and 
# assigning it a value of 1.0.

# Define the initializer method __init__ and pre-populate the movie list with a few movies. 
# Make sure the movies store is private.

# Define the play method, which sets the current_movie attribute to the first item in 
# the movies list.

# Define the list_movies method, which returns the list of movies in the MoviePlayer.

# We'll add the update_firmware version method, which checks for whether the new version 
# being provided is more recent than the current firmware version before updating.

# We then add a few test lines to the main method and run the script as shown in 

# Snippet 7.67:

#  player = MoviePlayer()
#  print("Movies currently on device:", player.list_movies())
 
#  player.update_firmware(2.0)
#  print("Updated player firmware version to", player.firmware_version)
 
#  player.play()
#  print("Currently playing", f"'{player.current_movie}'")
# Snippet 7.67

# We can run the script by entering python3 main.py in the terminal. The output should look 
# similar to Figure 7.6:

# workspace $ python3 main.py
# Movies currently on device: ['Frozen', 'Finding Nemo', 'Toy Story']
# Updated player firmware version to 2.0
# Currently playing 'Frozen'
# workspace $ 

# Figure 7.6

# Your code here
class MoviePlayer:
    firmware_version = 1.0

    def __init__(self):
        self.__movies = ["Frozen", "Finding Nemo", "Toy Story"]
        self.current_movie = None

    def play(self):
        self.current_movie = self.__movies[0]

    def list_movies(self):
        return self.__movies

    @classmethod
    def update_firmware(cls, new_version):
        if new_version > cls.firmware_version:
            cls.firmware_version = new_version

if __name__ == '__main__':
    player = MoviePlayer()
    print("Movies currently on device:", player.list_movies())

    player.update_firmware(2.0)
    print("Updated player firmware version to", player.firmware_version)

    player.play()
    print("Currently playing", f"'{player.current_movie}'")
