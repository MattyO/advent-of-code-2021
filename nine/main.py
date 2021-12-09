class Board():
    def __init__(self, cells):
        self.cells = cells

        for c in self.cells:
            c.board = self

        self._hashed_cells = { c: c for c in self.cells }

    def cells(self):
        return self._hashed_cells.values()

    def low_points(self):
        return [cell for cell in self.cells if cell.test_is_lowest()]

    def risk_levels(self):
        return [cell.value + 1 for cell in self.low_points()]

    def __getitem__(self, key):
        return self._hashed_cells.get(key, None)



class Cell():
    def __init__(self, x, y, value=None, board=None):
        self.x = x
        self.y = y
        self.value = value
        self.board = board

        self._possible_neighbors = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.y < other.y or self.x < other.x

    def __repr__(self):
        return f"Cell({self.x}, {self.y} val:{self.value})"

    def __hash__(self):
        return (self.y*10) + self.x

    def neighbors(self):
        return [self.board[cell] for cell in self.possible_neigbors() if self.board[cell] is not None ]

    def possible_neigbors(self):
        if self._possible_neighbors is None:
            self._possible_neighbors =  [
                Cell(self.x+1,  self.y),
                Cell(self.x-1,  self.y),
                Cell(self.x,    self.y + 1),
                Cell(self.x,    self.y - 1),
            ]

        return self._possible_neighbors

    def test_is_lowest(self):
        test=  sorted(self.neighbors()+ [self], key=lambda c: c.value)
        return self == sorted(self.neighbors()+ [self], key=lambda c: c.value)[0]


