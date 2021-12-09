import unittest
from collections import Counter

from main import parse_line, is_horizontal_or_vertical, points

class MainTest(unittest.TestCase):
    def test_parse_line(self):
        self.assertEqual(parse_line('0,9 -> 5,9'), [0,9, 5,9])

    def test_is_horizontal_or_vertical(self):
        self.assertTrue(is_horizontal_or_vertical(*parse_line(('0,9 -> 5,9'))))
        self.assertFalse(is_horizontal_or_vertical(*parse_line(('6,4 -> 2,0'))))

    def test_points(self):
        expected_points = [(7,0), (7,1),(7,2),(7,3),(7,4)]
        self.assertEqual(points(*parse_line('7,0 -> 7,4')), expected_points)

        expected_points = [(3,4),(2,4),(1,4)]
        self.assertEqual(points(*parse_line('3,4 -> 1,4')), expected_points)

    def test_example(self):
        with open('data/example.txt') as f:
            input_lines = f.readlines()

        line_coords = [parse_line(l) for l in input_lines if is_horizontal_or_vertical(*parse_line(l))]
        print(line_coords)
        all_the_line_points = [c for line in line_coords for c in line ]
        counts = Counter(all_the_line_points)
        print(counts)
        self.assertEqual(len([p for c, p in counts.items() if c > 1]), 5 )






