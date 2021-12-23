import unittest
from ai import checkwin

class TestSum(unittest.TestCase):
    def test_first_array(self):
        self.longMessage = True
        tiles = [[" ", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(checkwin(tiles,"X"),[0,0])
    def test_second_array(self):
        self.longMessage = True
        tiles = [[" ", " ", "X"], [" ", " ", "X"], [" ", " ", " "]]
        self.assertEqual(checkwin(tiles,"X"),[2,2])
    def test_third_array(self):
        self.longMessage = True
        tiles = [[" ", "X", "O"], [" ", "X", "X"], ["X", " ", " "]]
        self.assertEqual(checkwin(tiles,"X"),[1,0])
    def test_forth_array(self):
        self.longMessage = True
        tiles = [[" ", " ", " "], [" ", " ", "X"], [" ", " ", "X"]]
        self.assertEqual(checkwin(tiles,"X"),[0,2])
    def test_5_array(self):
        self.longMessage = True
        tiles = [["O", "X", "X"], [" ", " ", "O"], [" ", "X", " "]]
        self.assertEqual(checkwin(tiles,"X"),[1,1])
if __name__ == '__main__':
    unittest.main()
