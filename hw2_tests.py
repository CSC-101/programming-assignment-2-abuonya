import data
import hw2
import unittest
from data import Point
from data import Rectangle
from data import Duration
from data import Song

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
    def test_songs_shorter_than1(self):
        song1 = Song('Example1','SongTitle1', Duration(5,30))
        song2 = Song('Example2','SongTitle2', Duration(2,30))
        length_of_song = Duration(4,10)
        list_of_songs = [song1, song2]
        result = hw2.song_shorter_than(list_of_songs, length_of_song)
        expected = [song2]
        self.assertEqual(expected, result)

    def test_songs_shorter_than2(self):
        song1 = Song('Example1','SongTitle1', Duration(5,30))
        song2 = Song('Example2','SongTitle2', Duration(2,30))
        song3 = Song('Example3', 'SongTitle3', Duration(1, 43))
        song4 = Song('Example4', 'SongTitle4', Duration(0, 43))
        length_of_song = Duration(4,10)
        list_of_songs = [song1, song2, song3, song4]
        result = hw2.song_shorter_than(list_of_songs, length_of_song)
        expected = [song2, song3, song4]
        self.assertEqual(expected, result)


    # Part 4
    def test_running_time1(self):
        song1 = Song('Reality Club', 'Is It The Answer', Duration(4, 30))
        song2 = Song('Phum', 'LoverBoy', Duration(3, 29))
        song_list = [song1, song2]
        playlist = [0,1]
        result = hw2.running_time(song_list, playlist)
        expected = Duration(7,59)
        self.assertEqual(expected, result)

    def test_running_time2(self):
        song1 = Song('Reality Club', 'Is It The Answer', Duration(4, 30))
        song2 = Song('Phum', 'LoverBoy', Duration(3, 29))
        song3 = Song('Locked Out of Heaven', 'Bruno Mars', Duration(3, 10))
        song_list = [song1, song2, song3]
        playlist = [0,1,2,0,3,3,3,3]
        result = hw2.running_time(song_list, playlist)
        expected = Duration(15,39)
        self.assertEqual(expected, result)

    # Part 5
    def test_valid_route1(self):
        city_links = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'], ['atascadero', 'santa margarita'], ['atascadero', 'creston']]
        city_routes = ['san luis obispo', 'pismo beach', 'creston']
        result = hw2.valid_route(city_links, city_routes)
        expected = False
        self.assertEqual(expected, result)

    def test_valid_route2(self):
        city_links = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'], ['atascadero', 'santa margarita'], ['atascadero', 'creston']]
        city_routes = ['creston', 'atascadero', 'santa margarita', 'pismo beach']
        result = hw2.valid_route(city_links, city_routes)
        expected = False
        self.assertEqual(expected, result)

    def test_valid_route3(self):
        city_links = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'], ['atascadero', 'santa margarita'], ['atascadero', 'creston']]
        city_routes = ['san luis obispo', 'santa margarita']
        result = hw2.valid_route(city_links, city_routes)
        expected = False
        self.assertEqual(expected, result)

    # Part 6
    def test_longest_repetition1(self):
        list_of_integers = [1,2,3,4,4,4,4,4,4]
        result = hw2.longest_repetition(list_of_integers)
        expected = [3]
        self.assertEqual(expected, result)

    def test_longest_repetition2(self):
        list_of_integers = [1,2,3,4,4,4,4,4,4,5,6,7,9,99,99,99,99,99,99,99,99,99,100]
        result = hw2.longest_repetition(list_of_integers)
        expected = 13
        self.assertEqual(expected, result)

    def test_longest_repetition3(self):
        list_of_integers = []
        result = hw2.longest_repetition(list_of_integers)
        expected = None
        self.assertEqual(expected, result)







if __name__ == '__main__':
    unittest.main()
