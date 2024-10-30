import data
import hw2
import unittest
from data import Point
from data import Rectangle
from data import Duration

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        point1 = Point(2,5)
        point2 = Point(7,12)
        result = hw2.create_rectangle(point1, point2)
        expected = Rectangle(Point(2,12), Point(7,5))
        self.assertEqual(expected, result)

    def test_create_rectangle2(self):
        point1 = Point(2,2)
        point2 = Point(10,10)
        result = hw2.create_rectangle(point1, point2)
        expected = Rectangle(Point(2,10), Point(10,2))
        self.assertEqual(expected, result)

    # Part 2
    def test_shorter_duration_than1(self):
        duration1 = Duration(6,60)
        duration2 = Duration(10,30)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = True
        self.assertEqual(expected, result)

    def test_shorter_duration_than2(self):
        duration1 = Duration(15,60)
        duration2 = Duration(10,30)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = False
        self.assertEqual(expected, result)

    def test_shorter_duration_than3(self):
        duration1 = Duration(15, 60)
        duration2 = Duration(0, 30)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = False
        self.assertEqual(expected, result)
    # Part 3


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
