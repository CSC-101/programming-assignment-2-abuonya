import data
from data import Point
from data import Rectangle
from data import Duration


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




# Part 3


# Part 4


# Part 5


# Part 6
