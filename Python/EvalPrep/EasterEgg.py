class EasterEgg:
    """
    >>> puzzle = EasterEgg(7, 7, 'D4', 'eggs.txt')
    >>> puzzle.bunny()
    'D4'
    >>> puzzle.eggs() == {'A2', 'A3', 'A4', 'A6', 'A7', 'B1', 'B2', 'C2', 'C4', 'C7', 'D1', 'D2', 'D3', 'D5', 'D6', 'E2', 'E4', 'E7', 'F1', 'F2', 'G2', 'G3', 'G4', 'G6', 'G7'}
    True
    >>> print(puzzle)
    #OOO#OO
    OO#####
    #O#O##O
    OOOXOO#
    #O#O##O
    OO#####
    #OOO#OO
    >>> puzzle.isempty()
    False
    >>> puzzle.possible_moves() == {'B3', 'B5', 'C2', 'C6', 'D5', 'D6', 'D7', 'E2', 'E6', 'F3', 'F5'}
    True
    >>> print(puzzle.move('E2'))
    #OOO#OO
    OO#####
    #O#O##O
    OOO#OO#
    #X#O##O
    OO#####
    #OOO#OO
    >>> puzzle.bunny()
    'E2'
    >>> puzzle.eggs() == {'A2', 'A3', 'A4', 'A6', 'A7', 'B1', 'B2', 'C2', 'C4', 'C7', 'D1', 'D2', 'D3', 'D5', 'D6', 'E4', 'E7', 'F1', 'F2', 'G2', 'G3', 'G4', 'G6', 'G7'}
    True
    >>> puzzle.isempty()
    False
    >>> puzzle.possible_moves() == {'C1', 'C3', 'D4', 'E3', 'E4', 'E5', 'E6', 'E7', 'F4', 'G1', 'G3'}
    True
    >>> puzzle.move('B3')
    Traceback (most recent call last):
    AssertionError: invalid move
    >>> puzzle.move('B2')
    Traceback (most recent call last):
    AssertionError: invalid move
    >>> print(puzzle.move('G3').move('F1').move('E3').move('G2').move('G4'))
    #OOO#OO
    OO#####
    #O#O##O
    OOO#OO#
    ###O##O
    #O#####
    ###X#OO
    >>> puzzle.possible_moves() == {'E3', 'E5', 'F2', 'F6', 'G5', 'G6', 'G7'}
    True
    >>> print(puzzle.move('F2').move('E4').move('D2').move('B1').move('A3'))
    #OXO#OO
    #O#####
    #O#O##O
    O#O#OO#
    ######O
    #######
    #####OO
    >>> print(puzzle.move('C2').move('C4').move('B2').move('D1').move('D3'))
    #O#O#OO
    #######
    ######O
    ##X#OO#
    ######O
    #######
    #####OO
    >>> print(puzzle.move('B4').move('A2').move('A4').move('A6').move('A7'))
    ######X
    #######
    ######O
    ####OO#
    ######O
    #######
    #####OO
    >>> print(puzzle.move('C6').move('C7').move('D5').move('E7').move('G6'))
    #######
    #######
    #######
    #####O#
    #######
    #######
    #####XO
    >>> print(puzzle.move('G7').move('F5').move('D6').move('D7'))
    #######
    #######
    #######
    ######X
    #######
    #######
    #######
    >>> puzzle.isempty()
    True
    """

    # ======================================================================
    # HELPER FUNCTIONS
    @staticmethod
    def letter_to_num(letter):
        return ord(letter) - ord('A')
    @staticmethod
    def num_to_letter(num):
        return chr(num + ord('A'))
    @staticmethod
    def to_num_coords(str_coords):
        return EasterEgg.letter_to_num(str_coords[0]), int(str_coords[1:]) - 1
    @staticmethod
    def to_letter_coords(num_coords):
        return f'{EasterEgg.num_to_letter(num_coords[0])}{str(num_coords[1] + 1)}'
    #======================================================================




    def __init__(self, m, n, start, file_name):
        self.m = m
        self.n = n
        self.bunny_pos = EasterEgg.to_num_coords(start)

        self.board = []
        for _ in range(m):
            self.board.append(['#'] * n)


        with open(file_name, 'r', encoding='UTF-8') as invoer:
            for line in invoer:
                line = line.strip()
                coords = EasterEgg.to_num_coords(line)
                self.board[coords[0]][coords[1]] = 'O'

        self.board[self.bunny_pos[0]][self.bunny_pos[1]] = 'X'

    def __str__(self):
        return '\n'.join((''.join(line) for line in self.board))


    def bunny(self):
        return EasterEgg.to_letter_coords(self.bunny_pos)


    def eggs(self):
        eggs = set()

        for row in range(self.m):
            for col in range(self.n):
                if self.board[row][col] == 'O':
                    eggs.add(EasterEgg.to_letter_coords((row, col)))

        return eggs


    def possible_moves(self):
        moves = set()

        # all eastwards
        for right in range(self.bunny_pos[1]+1, self.n):
            moves.add(EasterEgg.to_letter_coords((self.bunny_pos[0], right)))

        # knight moveset
        bpos = self.bunny_pos
        for i in range(-1, 2, 2):
            for j in range(-2, 3, 4):
                if 0 <= bpos[0] + i < self.m and 0 <= bpos[1] + j < self.n:
                    moves.add(EasterEgg.to_letter_coords((bpos[0] + i, bpos[1] + j)))
                if 0 <= bpos[0] + j < self.m and 0 <= bpos[1] + i < self.n:
                    moves.add(EasterEgg.to_letter_coords((bpos[0] + j, bpos[1] + i)))
        # moves.add(EasterEgg.to_letter_coords((bpos[0] + 2, bpos[1] + 1)))
        # moves.add(EasterEgg.to_letter_coords((bpos[0] + 2, bpos[1] - 1)))
        # moves.add(EasterEgg.to_letter_coords((bpos[0] - 2, bpos[1] + 1)))
        # moves.add(EasterEgg.to_letter_coords((bpos[0] - 2, bpos[1] - 1)))
        # moves.add(EasterEgg.to_letter_coords((bpos[0] + 1, bpos[1] + 2)))
        # moves.add(EasterEgg.to_letter_coords((bpos[0] + 1, bpos[1] - 2)))
        # moves.add(EasterEgg.to_letter_coords((bpos[0] - 1, bpos[1] + 2)))
        # moves.add(EasterEgg.to_letter_coords((bpos[0] - 1, bpos[1] - 2)))

        return moves


    def move(self, p):
        assert p in self.possible_moves(), 'invalid move'
        pos = EasterEgg.to_num_coords(p)
        self.board[pos[0]][pos[1]] = 'X'
        self.board[self.bunny_pos[0]][self.bunny_pos[1]] = '#'
        self.bunny_pos = pos

        return self


    def isempty(self):
        return len(self.eggs()) == 0

















if __name__ == '__main__':
    import doctest
    doctest.testmod()



