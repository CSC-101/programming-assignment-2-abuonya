import data
from data import Point
from data import Rectangle
from data import Duration
from data import Song


# Write your functions for each part in the space below.

# Part 1
    # Purpose: Find the missing two corners of a rectangle (top left and bottom right points) given two other points (top right and bottom left).
    # Function Name: create_rectangle
    # input: Two different points of a rectangle
    # output: string representation of class Rectangle
    # If I were a computer...just swap the x/y coordinates!
def create_rectangle(topright: Point, bottomleft: Point) -> str:
    # Finding the top left coordinate
    top_left_x = topright.x
    top_left_y = bottomleft.y
    top_left = Point(top_left_x, top_left_y)

    # Find the bottom right coordinate
    bottom_right_x = bottomleft.x
    bottom_right_y = topright.y
    bottom_right = Point(bottom_right_x, bottom_right_y)

    # output the rectangle
    print (Rectangle(top_left, bottom_right))
    return Rectangle(top_left, bottom_right)

# Part 2
    # Purpose: Find if the first duration parameter is shorter than the second parameter.
    # Function Name: shorter_duration_than
    # input: Two different parameters of type Duration
    # output: boolean indicating true or false
    # If I were a computer...convert both durations into seconds. Compare if duration 1 in seconds is less/greater than duration 2 in seconds.
def shorter_duration_than(duration1: Duration, duration2: Duration) -> bool:
    #convert minutes to seconds
    duration1_in_seconds = (duration1.minutes * 60) + duration1.seconds
    duration2_in_seconds = (duration2.minutes * 60) + duration2.seconds

    if duration1_in_seconds < duration2_in_seconds:
        return True
    else:
        return False

# Part 3
    # Purpose: Find a list of all songs with a duration less than the provided duration parameter.
    # Function Name: songs_shorter_than
    # input: list from class Song list[Song] and one parameter of duration
    # output: a list of strings
    # If I were a computer...take list of songs, create a for loop that checks the durations of each song in the list and compares if its less than the provided duration. If it is, append it to a new list of songs. Return the new list when it is done.
def song_shorter_than(songs: list[Song], song_length: Duration) -> list:
    new_songlist = []
    for song in songs:
        if song.duration.minutes < song_length.minutes:
            new_songlist.append(song)
    return new_songlist

# Part 4



# Part 5
    # Purpose: find if a route is valid by passing through each intermediate city and seeing if they cross one another.
    # Function Name: valid_route
    # input: a list of city links, a list of city names (that user wants to pass through)
    # output: a boolean determining if the route is valid (true/false)
    # If I were a computer...uhummmmmm
def valid_route(city_links: list[list[str]], city_list: list[str]) -> bool:



# Part 6
