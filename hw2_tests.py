import data
import hw2
import unittest
from data import Point
from data import Rectangle

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        point1 = Point(2,5)
        point2 = Point(7,12)
        result = hw2.create_rectangle(point1, point2)
        expected = Rectangle((2,12),(7,5))
        self.assertEqual(expected, result)

    # Part 2


    # Part 3


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
