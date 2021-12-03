import unittest
from collections import Counter

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

    def test_most_common_defaults_to_one(self):
        self.assertEqual(main.most_common(Counter('1100')), '1')
        self.assertEqual(main.most_common(Counter('0011')), '1')

    def test_lest_common(self):
        with open("data/example.txt") as f:
            input_strings = [l.strip() for l in f.readlines()]
        position_counts = main.position_counts(input_strings)

        self.assertEqual(main.least_common(position_counts[0]), '0')

    def test_lest_common_default_to_0(self):
        self.assertEqual(main.least_common(Counter('1100')), '0')
        self.assertEqual(main.least_common(Counter('0011')), '0')
        self.assertEqual(main.least_common(Counter('011')), '0')

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
        self.assertEqual(gamma * epsilon, 1082324 )

    def test_rating(self):
        with open("data/example.txt") as f:
            input_strings = [l.strip() for l in f.readlines()]

        oxygen = main.to_digit(main.rating(input_strings, main.most_common))
        co2 = main.to_digit(main.rating(input_strings, main.least_common))

        self.assertEqual(oxygen, 23)
        self.assertEqual(co2, 10)

        self.assertEqual(oxygen * co2, 230)

    def test_rating_puzzle(self):
        with open("data/puzzle.txt") as f:
            input_strings = [l.strip() for l in f.readlines()]

        oxygen = main.to_digit(main.rating(input_strings, main.most_common))
        co2 = main.to_digit(main.rating(input_strings, main.least_common))

        self.assertEqual(oxygen, 486)
        self.assertEqual(co2, 2784)

        self.assertEqual(oxygen * co2, 230)



