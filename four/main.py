import itertools

class Position():
    def __init__(self, x, y, number=None, is_marked=False):
        self.is_marked = is_marked
        self.x = x
        self.y = y
        self.number = number

    def __repr__(self):
        return f'Position({self.x}, {self.y} {self.number}, {self.is_marked})'

    def __eq__(self, other_position):
        return  self.x == other_position.x  \
                and self.y == other_position.y \
                and self.number == other_position.number


def create_boards(input_lines):
    board_index = 0
    boards = [Board(board_index)]
    row = 0
    for line in input_lines:
        if line == '\n':
            row=0
            board_index+=1
            boards.append(Board(board_index))
            continue

        for i, number in enumerate(line.strip().split()):
            boards[-1].add_position(Position(row, i, int(number)))
        row += 1

    return boards

class Board():
    def __init__(self, index=None):
        self.positions= []
        self.index = index

    def __contains__(self, other_position):
        return any(p == other_position for p in self.positions)

    def mark_position(self, number):
        for position in self.positions:
            if position.number == number:
                position.is_marked = True

    def marked_positions(self):
        return [p for p in self.positions if p.is_marked == True]

    def add_position(self, position):
        self.positions.append(position)

    def has_marked(self, key):
        sorted_positions = sorted(self.positions, key=key)
        column_groups = itertools.groupby(sorted_positions, key)

        for column, group in column_groups:
            if all(p.is_marked for p in group):
                return True

        return False


    def has_marked_column(self):
        return self.has_marked(lambda p: p.y)

    def has_marked_row(self):
        return self.has_marked(lambda p: p.x)


