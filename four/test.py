import unittest
from main import Position, Board, create_boards

class MainTest(unittest.TestCase):
    def setUp(self):
        with open('data/example.txt') as f:
            self.input_lines = f.readlines()

        with open('data/puzzle.txt') as f:
            self.input_lines_puzzle = f.readlines()


    def test_two_positions_are_equal(self):
        self.assertEqual(Position(1,1), Position(1,1))
        self.assertNotEqual(Position(1,2), Position(1,1))
        self.assertNotEqual(Position(2,1), Position(1,1))

    def test_add_position(self):
        board = Board()
        board.add_position(Position(0,0))
        self.assertListEqual(board.positions, [Position(0,0)])

    def test_add_position(self):
        board = Board()
        board.add_position(Position(0,0))
        self.assertListEqual(board.positions, [Position(0,0)])

    def test_mark_position(self):
        board = Board()
        board.add_position(Position(0,0,number=2))

        self.assertListEqual(board.positions, [Position(0,0, number=2)])
        self.assertEqual(board.positions[0].is_marked, False)
        board.mark_position(2)
        self.assertEqual(board.positions[0].is_marked, True)


    def test_marked_positions(self):
        board = Board()
        board.add_position(Position(0,0,number=2))
        board.mark_position(2)

        self.assertListEqual(board.marked_positions(), [Position(0,0,2)])

    def test_create_boards(self):
        boards = create_boards(self.input_lines[2:])

        self.assertEqual(len(boards), 3)
        self.assertEqual(len(boards[0].positions), 25)
        self.assertTrue(Position(0,0,22) in boards[0])
        self.assertTrue(Position(4,4,19) in boards[0])

    def test_has_marked_row(self):
        board = Board()
        board.add_position(Position(0,0, 1))
        board.add_position(Position(0,1, 2))
        board.add_position(Position(1,0, 3, True))
        board.add_position(Position(1,1, 4, True))

        self.assertTrue(board.has_marked_row())


    def test_has_marked_column(self):
        board = Board()
        board.add_position(Position(0,0, 1))
        board.add_position(Position(0,1, 2, True))
        board.add_position(Position(1,0, 3))
        board.add_position(Position(1,1, 4, True))

        self.assertTrue(board.has_marked_column())

    def test_example(self):
        bingo_numbers = [int(n) for n in self.input_lines[0].strip().split(',')]
        boards = create_boards(self.input_lines[2:])
        winning_board = None
        winning_number= None

        for number in bingo_numbers:
            for board in boards:
                board.mark_position(number)
                winning_number = number

            winning_boards = list(filter(lambda b: b.has_marked_row() or b.has_marked_column(), boards))
            if len(winning_boards) > 0:
                break

        self.assertEqual(boards[2], winning_boards[0])

        ummarked_sum = sum(p.number for p in winning_boards[0].positions if not p.is_marked)
        self.assertEqual(ummarked_sum, 188 )
        self.assertEqual(winning_number , 24)
        self.assertEqual(winning_number*ummarked_sum, 4512)

    def test_puzzle(self):
        bingo_numbers = [int(n) for n in self.input_lines_puzzle[0].strip().split(',')]
        boards = create_boards(self.input_lines_puzzle[2:])
        winning_board = None
        winning_number= None

        for number in bingo_numbers:
            for board in boards:
                board.mark_position(number)
                winning_number = number

            winning_boards = list(filter(lambda b: b.has_marked_row() or b.has_marked_column(), boards))
            if len(winning_boards) > 0:
                break

        ummarked_sum = sum(p.number for p in winning_boards[0].positions if not p.is_marked)
        self.assertEqual(ummarked_sum, 640)
        self.assertEqual(winning_number , 46)
        self.assertEqual(winning_number*ummarked_sum, 29440 )

    def test_example_pt_2(self):
        bingo_numbers = [int(n) for n in self.input_lines[0].strip().split(',')]
        boards = create_boards(self.input_lines[2:])
        winning_number = None
        winning_numbers= []

        for number in bingo_numbers:
            for board in boards:
                board.mark_position(number)
                winning_number = number

            winning_boards = list(filter(lambda b: b.has_marked_row() or b.has_marked_column(), boards))
            winning_numbers += list(set(b.index for b in winning_boards) - set(winning_numbers))
            if len(winning_boards) == len(boards):
                break

        losing_board = next(b for b in boards if b.index == winning_numbers[-1] )

        ummarked_sum = sum(p.number for p in losing_board.positions  if not p.is_marked)
        self.assertEqual(losing_board.index, 1)
        self.assertEqual(ummarked_sum, 148)
        self.assertEqual(winning_number , 13)
        self.assertEqual(winning_number*ummarked_sum, 1924)

    def test_puzzle_pt_2(self):
        bingo_numbers = [int(n) for n in self.input_lines_puzzle[0].strip().split(',')]
        boards = create_boards(self.input_lines_puzzle[2:])
        winning_numbers= []

        for number in bingo_numbers:
            for board in boards:
                board.mark_position(number)
                winning_number = number

            winning_boards = list(filter(lambda b: b.has_marked_row() or b.has_marked_column(), boards))
            winning_numbers += list(set(b.index for b in winning_boards) - set(winning_numbers))
            if len(winning_boards) == len(boards):
                break

        losing_board = next(b for b in boards if b.index == winning_numbers[-1] )
        ummarked_sum = sum(p.number for p in losing_board.positions  if not p.is_marked)

        self.assertEqual(ummarked_sum, 267)
        self.assertEqual(winning_number , 52)
        self.assertEqual(winning_number*ummarked_sum, 13884)

