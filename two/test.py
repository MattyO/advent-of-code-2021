from unittest import TestCase

import main

from main import Poisition

class MainTest(TestCase):

    def test_command_forward(self):
        command = ['forward 4']
        self.assertEqual(main.compute_position(command), Poisition(4, 0))

    def test_command_down(self):
        command = ['down 4']
        self.assertEqual(main.compute_position(command), Poisition(0, 4))

    def test_command_down_and_up(self):
        command = ['down 4', 'up 2']
        self.assertEqual(main.compute_position(command), Poisition(0, 2))

    def test_commands(self):
        with open('data/example.txt') as f:
            input_commands = f.readlines()

        ending_poisition = main.compute_position(input_commands)
        self.assertEqual(ending_poisition , Poisition(15, 10))
        self.assertEqual(ending_poisition.horizontal * ending_poisition.depth , 150)

    def test_commands_puzzle(self):
        with open('data/puzzle.txt') as f:
            input_commands = f.readlines()

        ending_poisition = main.compute_position(input_commands)
        self.assertEqual(ending_poisition , Poisition(1890,1172))
        self.assertEqual(ending_poisition.horizontal * ending_poisition.depth , 2215080)



