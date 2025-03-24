
class Hermit:
    """
    >>> board = Hermit(4)
    >>> print(board)
    . . . .
    . . . .
    . . . .
    . . . .
    >>> board.positions((0, 0), 'H') == {(0, 0), (0, 1)}
    True
    >>> board.isvalid('R', (0, 0))
    True
    >>> board.isvalid('R', (0, 1))
    True
    >>> print(board.move('R', (0, 0), 'H'))
    R R . .
    . . . .
    . . . .
    . . . .
    >>> print(board.move('R', (1, 2), 'V'))
    Traceback (most recent call last):
    AssertionError: invalid move
    >>> print(board.move('B', (0, 2), 'U').move('Y', (1, 2), 'U'))
    R R B .
    . . Y .
    . . . .
    . . . .
    >>> print(board.move('R', (3, 1), 'U').move('Y', (3, 2), 'H'))
    R R B .
    . . Y .
    . . . .
    . R Y Y
    >>> print(board.move('R', (1, 3), 'V').move('B', (2, 0), 'H'))
    R R B .
    . . Y R
    B B . R
    . R Y Y
    >>> board.possible_moves()
    {('Y', (1, 0), 'U'), ('Y', (3, 0), 'U')}
    >>> print(board.move('Y', (3, 0), 'U'))
    R R B .
    . . Y R
    B B . R
    Y R Y Y
    >>> board.possible_moves()
    {('Y', (1, 0), 'U')}
    >>> print(board.move('Y', (1, 0), 'U'))
    R R B .
    Y . Y R
    B B . R
    Y R Y Y
    >>> board.possible_moves()
    set()
    """

    def __init__(self, n):
        self.n = n
        # deep initialization of array so that the inner arrays arent all the same object
        self.board_data = []
        for _ in range(n):
            self.board_data.append(['.']*n)

    def __str__(self):
        return '\n'.join([' '.join(self.board_data[r]) for r in range(self.n)])


    def positions(self, pos, p):
        if p == 'V':
            return {pos, (pos[0]+1, pos[1])}
        if p == 'H':
            return {pos, (pos[0], pos[1]+1)}
        return {pos}

    def isvalid(self, c, pos):
        rij = pos[0]
        kol = pos[1]
        if not 0 <= rij < self.n or not 0 <= kol < self.n or self.board_data[rij][kol] != '.':
            return False
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if (0 <= rij+i < self.n and
                    0 <= kol+j < self.n and
                    self.board_data[rij+i][kol+j] == c):
                    return False
        return True

    # helper function to account for placement
    def isvalidwithplacement(self, c, pos, p):
        valid = True
        for position in self.positions(pos, p):
            valid &= self.isvalid(c, position)
        return valid



    def move(self, c, pos, p):
        positions = self.positions(pos, p)

        for position in positions:
            assert self.isvalid(c, position), 'invalid move'

        for position in positions:
            self.board_data[position[0]][position[1]] = c

        return self

    def possible_moves(self):
        moves = set()
        for r in range(self.n):
            for c in range(self.n):
                if self.board_data[r][c] == '.':
                    for color in 'YBR':
                        for p in 'UHV':
                            if self.isvalidwithplacement(color, (r, c), p):
                                moves.add((color, (r, c), p))
        return moves
    # https://miro.medium.com/v2/resize:fit:962/1*YoTPCR_l1ApgGGfMp6ZzmQ.png




if __name__ == '__main__':
    import doctest
    doctest.testmod()