import unittest

from main import Board, Cell

class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_possible_neighbors(self):
        cell = Cell(0,0)
        expected_possible_neighbors = [Cell(-1,0), Cell(1,0), Cell(0,1), Cell(0,-1)]
        self.assertListEqual(
                sorted(cell.possible_neigbors()),
                sorted(expected_possible_neighbors))

    def test_neighbors(self):
        board = Board([Cell(0,0), Cell(0,1)])
        self.assertListEqual(board.cells[0].neighbors(), [Cell(0,1)])

    def test_is_lowest(self):
        board = Board([Cell(0,0, 1), Cell(0,1, 2)])

        self.assertTrue(board.cells[0].test_is_lowest())
        self.assertFalse(board.cells[1].test_is_lowest())

    def test_board_low_points(self):
        board = Board([Cell(0,0, 1), Cell(0,1, 2)])
        self.assertLessEqual(board.low_points(), [Cell(0,0)])

    def test_board_risk_levels(self):
        board = Board([Cell(0,0, 1), Cell(0,1, 2)])
        self.assertListEqual(board.risk_levels(), [2])

    def test_example(self):
        with open('data/example.txt') as f:
            board = Board([Cell(x, y, int(value))
                for y, line in enumerate(f.readlines())
                    for x, value in enumerate(line.strip())])

        self.assertListEqual(board.risk_levels(), [2,1,6,6])
        self.assertEqual(sum(board.risk_levels()), 15)

    def test_puzzle(self):
        with open('data/puzzle.txt') as f:
            board = Board([Cell(x, y, int(value))
                for y, line in enumerate(f.readlines())
                    for x, value in enumerate(line.strip())])

        self.assertEqual(sum(board.risk_levels()), 15)





