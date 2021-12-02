from unittest import TestCase

import main

class TestMain(TestCase):
    def test_increase_or_decrease(self):
        self.assertEqual(main.increase_or_decrease(1,1), 'no change')
        self.assertEqual(main.increase_or_decrease(1,2), 'increase')
        self.assertEqual(main.increase_or_decrease(2,1), 'decrease')

    def test_count_items(self):
        input_array = ['increase', 'decrease', 'increase']
        self.assertEqual(main.count_items(input_array, 'increase'), 2)
        self.assertEqual(main.count_items(input_array, 'decrease'), 1)

    def test_find_changes_example_input(self):
        with open('data/one_test_input.txt') as f:
            measurement_input = [int(l) for l in f.readlines()]

        self.assertEqual(main.count_items(main.find_changes(measurement_input), 'increase'), 7)

    def test_find_changes(self):
        with open('data/one_problem_input.txt') as f:
            measurement_input = [int(l) for l in f.readlines()]

        self.assertEqual(main.count_items(main.find_changes(measurement_input), 'increase'), 1711)

    def test_windowed_sum(self):
        with open('data/one_test_input.txt') as f:
            measurement_input = [int(l) for l in f.readlines()]

        expected_array = [607, 618, 618, 617, 647, 716, 769, 792,]
        self.assertEqual(main.windowed_increase(measurement_input), expected_array)


    def test_windowed_sum_increase(self):
        with open('data/one_test_input.txt') as f:
            measurement_input = [int(l) for l in f.readlines()]

        self.assertEqual(main.count_items(main.find_changes(main.windowed_increase(measurement_input)), 'increase'), 5)

    def test_windowed_sum_increase_problem(self):
        with open('data/one_problem_input.txt') as f:
            measurement_input = [int(l) for l in f.readlines()]

        self.assertEqual(main.count_items(main.find_changes(main.windowed_increase(measurement_input)), 'increase'), 5)
