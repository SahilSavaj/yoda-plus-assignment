import unittest
from main import parse_string


class TestParseString(unittest.TestCase):
    def test_simple_range(self):
        self.assertEqual(parse_string("1-3"), [1, 2, 3])

    def test_single_numbers(self):
        self.assertEqual(parse_string("5"), [5])

    def test_multiple_ranges(self):
        self.assertEqual(parse_string("1-2,4-5"), [1, 2, 4, 5])

    def test_ranges_and_numbers(self):
        self.assertEqual(parse_string("1-2,4,6-7"), [1, 2, 4, 6, 7])

    def test_single_and_range(self):
        self.assertEqual(parse_string("3,5-6"), [3, 5, 6])

    def test_spaces(self):
        self.assertEqual(parse_string("1 -3, 5,7 - 9"), [1, 2, 3, 5, 7, 8, 9])

    def test_duplicate_numbers(self):
        self.assertEqual(parse_string("1,1-2,2"), [1, 1, 2, 2])

    def test_empty_string(self):
        self.assertEqual(parse_string(""), [])

    def test_leading_and_trailing_commas(self):
        self.assertEqual(parse_string(",1-2,3,"), [1, 2, 3])

    def test_invalid_input(self):
        self.assertEqual(parse_string("a,1-b"), [])


if __name__ == "__main__":
    unittest.main()
