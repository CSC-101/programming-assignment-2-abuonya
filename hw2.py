import data
from data import Point
from data import Rectangle


# Write your functions for each part in the space below.

# Part 1
    # Purpose: Find the missing two corners of a rectangle (top left and bottom right points) given two other points (top right and bottom left).
    # Function Name: create_rectangle
    # input: Two different points of a rectangle
    # output: string representation of class Rectangle
def create_rectangle(topright: Point, bottomleft: Point) -> str:
    x_coordinate = topright.x
    print(x_coordinate)

    # Finding the top left coordinate
    top_left_x = topright.x
    top_left_y = bottomleft.y
    top_left = Point(top_left_x, top_left_y)

    # Find the bottom right coordinate
    bottom_right_x = bottomleft.x
    bottom_right_y = topright.y













# Part 2


# Part 3


# Part 4


# Part 5


# Part 6
