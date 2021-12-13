import unittest
from functools import reduce

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

        self.assertEqual(sum(board.risk_levels()), 631)

    def test_cell_hash(self):
        test_hash = {}
        test_hash[Cell(0,0)] = 'value'
        self.assertEqual(test_hash[Cell(0,0)], 'value')

    def test_board_hash(self):
        board = Board([Cell(0,0)])
        self.assertEqual(board[Cell(0,0)], Cell(0,0))

    def test_board_hash_returns_none_when_no_cell_is_present(self):
        board = Board([Cell(0,0)])
        self.assertEqual(board[Cell(0,1)], None)

    def test_find_connected_group(self):
        board = Board([Cell(0,0), Cell(0,1), Cell(0,2, 9), Cell(0,3)])
        connected_group = board.connected_group(Cell(0,0))
        self.assertListEqual(connected_group, [Cell(0,0), Cell(0,1)])

    def test_find_connected_group_2(self):
        board = Board([Cell(0,0), Cell(0,1), Cell(0,2), Cell(0,3, 9), Cell(0,4)])
        connected_group = board.connected_group(Cell(0,0))
        self.assertListEqual(connected_group, [Cell(0,0), Cell(0,1), Cell(0,2)])

    def test_find_basin_sizes_example(self):
        with open('data/example.txt') as f:
            board = Board([Cell(x, y, int(value))
                for y, line in enumerate(f.readlines())
                    for x, value in enumerate(line.strip())])

        basins = board.find_basins()
        basins_sizes = [len(b) for b in basins.values()]
        basins_sizes.reverse()
        largest_3 = basins_sizes[:3]

        self.assertEqual(len(basins.values()), 4)
        self.assertEqual(sorted(basins_sizes), sorted([3, 9, 14, 9]))
        self.assertEqual(sorted(largest_3), sorted([9, 14, 9]))
        self.assertEqual(reduce(lambda x,y: x*y, largest_3), 1134)


    def test_find_basin_sizes_puzzle(self):
        with open('data/puzzle.txt') as f:
            board = Board([Cell(x, y, int(value))
                for y, line in enumerate(f.readlines())
                    for x, value in enumerate(line.strip())])

        basins = board.find_basins()
        basins_sizes = sorted([len(b) for b in basins.values()])
        basins_sizes.reverse()
        largest_3 = basins_sizes[:3]

        self.assertEqual(len(basins.values()), 252)
        #self.assertEqual(sorted(basins_sizes), sorted([3, 9, 14, 9]))
        self.assertEqual(sorted(largest_3), sorted([92, 94, 95]))
        self.assertEqual(reduce(lambda x,y: x*y, largest_3), 5915)


