import unittest

import main

class MainTest(unittest.TestCase):

    def test_position_counts(self):
        with open("data/example.txt") as f:
            input_strings = [l.strip() for l in f.readlines()]
        self.assertEqual(main.position_counts(input_strings)[0]['0'], 5)
        self.assertEqual(main.position_counts(input_strings)[0]['1'], 7)

    def test_most_common(self):
        with open("data/example.txt") as f:
            input_strings = [l.strip() for l in f.readlines()]
        position_counts = main.position_counts(input_strings)

        self.assertEqual(main.most_common(position_counts[0]), '1')

    def test_lest_common(self):
        with open("data/example.txt") as f:
            input_strings = [l.strip() for l in f.readlines()]
        position_counts = main.position_counts(input_strings)

        self.assertEqual(main.least_common(position_counts[0]), '0')

    def test_rates(self):
        with open("data/example.txt") as f:
            input_strings = [l.strip() for l in f.readlines()]
        position_counts = main.position_counts(input_strings)

        gamma, epsilon = main.rates(position_counts)
        self.assertEqual(gamma, '10110')
        self.assertEqual(epsilon ,'01001')

    def test_to_digit(self):
        self.assertEqual(main.to_digit('10110'), 22)
        self.assertEqual(main.to_digit('01001'), 9)

    def test_example(self):
        with open("data/example.txt") as f:
            input_strings = [l.strip() for l in f.readlines()]
        position_counts = main.position_counts(input_strings)

        gamma, epsilon = main.rates(position_counts)
        gamma, epsilon = map(lambda n: main.to_digit(n), [gamma, epsilon])
        self.assertEqual(gamma * epsilon, 198)

    def test_puzzle(self):
        with open("data/puzzle.txt") as f:
            input_strings = [l.strip() for l in f.readlines()]
        position_counts = main.position_counts(input_strings)

        gamma, epsilon = main.rates(position_counts)
        gamma, epsilon = map(lambda n: main.to_digit(n), [gamma, epsilon])
        self.assertEqual(gamma * epsilon, 198)

