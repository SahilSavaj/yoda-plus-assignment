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
        with self.assertRaises(Exception):
            parse_string("a,1-b")

    def test_double_dot_delimiter(self):
        self.assertEqual(parse_string("1..3"), [1, 2, 3])
        self.assertEqual(parse_string("10..12"), [10, 11, 12])

    def test_tilde_delimiter(self):
        self.assertEqual(parse_string("4~6"), [4, 5, 6])
        self.assertEqual(parse_string("7~7"), [7])

    def test_to_delimiter(self):
        self.assertEqual(parse_string("5 to 7"), [5, 6, 7])
        self.assertEqual(parse_string("12 to 15"), [12, 13, 14, 15])

    def test_mixed_delimiters(self):
        self.assertEqual(parse_string("1-2,3..4,5~6,7 to 8"), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_mixed_with_singles_and_spaces(self):
        self.assertEqual(
            parse_string(" , 1-3 ,5 to 7,,7..9,9~11 "),
            [1, 2, 3, 5, 6, 7, 7, 8, 9, 9, 10, 11],
        )

    def test_overlapping_ranges(self):
        self.assertEqual(parse_string("1-3,2..4"), [1, 2, 3, 2, 3, 4])

    def test_single_value_ranges(self):
        self.assertEqual(parse_string("4-4,6..6,8~8,10 to 10"), [4, 6, 8, 10])

    def test_invalid_range(self):
        with self.assertRaises(Exception):
            parse_string("9 to 5")


if __name__ == "__main__":
    unittest.main()
