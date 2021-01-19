import sys
import os

from unittest import TestCase, TestSuite, TextTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from wordhunt import WordHunt

class WordGridTestCase(TestCase):
    def setUp(self):
        self.wh_coord_test = WordHunt("colors.pzl")
        self.wh_coord_test.patternSearch()

    def test_correct_coordinates(self):
        self.assertEqual(self.wh_coord_test._word_coords['YELLOW'], ["(6,5)", "(11,5)"])
        self.assertEqual(self.wh_coord_test._word_coords['RED'], ["(9,2)", "(7,2)"])
        self.assertEqual(self.wh_coord_test._word_coords['BLUE'], ["(4,6)", "(7,6)"])

    def test_check_duplicates(self):
        self.assertEqual(len(self.wh._word_coords), 4)


class DuplicateTest(TestCase):
    def test_check_duplicates(self):
        self.wh = WordHunt("test/duplicate.pzl")
        self.wh.patternSearch()
        self.assertEqual(len(self.wh._word_coords), 1)


def suite():
    suite = TestSuite()
    suite.addTest(WordGridTestCase("test_correct_coordinates"))
    return suite


if __name__ == "__main__":
    runner = TextTestRunner()
    runner.run(suite())
