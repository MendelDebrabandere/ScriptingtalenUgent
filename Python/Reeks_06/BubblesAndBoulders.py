
class Puzzle:
    """
    >>> puzzle = Puzzle('puzzle.txt')
    >>> puzzle.rows
    4
    >>> puzzle.columns
    4
    >>> puzzle.regions == {'A', 'B', 'C', 'D'}
    True
    >>> puzzle.squares('A') == {(0, 1), (0, 2)}
    True
    >>> puzzle.squares('B') == {(0, 3), (1, 3), (2, 2), (2, 3), (3, 3)}
    True
    >>> puzzle.squares('C') == {(1, 0), (2, 0), (3, 0)}
    True
    >>> puzzle.squares('D') == {(1, 1), (1, 2), (2, 1), (3, 1)}
    True
    >>> puzzle.squares('E')
    Traceback (most recent call last):
    AssertionError: invalid region
    >>> puzzle.bubble('A')
    >>> puzzle.boulder('B')
    >>> puzzle.bubble('E')
    Traceback (most recent call last):
    AssertionError: invalid region
    >>> print(puzzle)
    #...
    ....
    ....
    ..#.
    >>> puzzle.issolved()
    False
    >>> puzzle.isempty(0, 1)
    True
    >>> print(puzzle.put_bubble(0, 1))
    #O..
    ....
    ....
    ..#.
    >>> puzzle.bubble('A')
    (0, 1)
    >>> puzzle.boulder('A')
    >>> puzzle.isempty(0, 1)
    False
    >>> puzzle.isempty(0, 2)
    True
    >>> puzzle.put_bubble(0, 2)     # second bubble in region A
    Traceback (most recent call last):
    AssertionError: invalid position
    >>> puzzle.isempty(2, 0)
    True
    >>> puzzle.put_boulder(2, 0)    # boulder floats above empty square
    Traceback (most recent call last):
    AssertionError: invalid position
    >>> puzzle.isempty(3, 0)
    True
    >>> print(puzzle.put_boulder(3, 0))
    #O..
    ....
    ....
    *.#.
    >>> puzzle.bubble('C')
    >>> puzzle.boulder('C')
    (3, 0)
    >>> puzzle.issolved()
    False
    >>> puzzle.put_boulder(2, 0)    # second boulder in region C
    Traceback (most recent call last):
    AssertionError: invalid position
    >>> puzzle.put_bubble(3, 2)     # bubble in green square
    Traceback (most recent call last):
    AssertionError: invalid position
    >>> puzzle.put_bubble(2, 2)     # bubble floats below empty square
    Traceback (most recent call last):
    AssertionError: invalid position
    >>> puzzle.put_boulder(1, 2)    # boulder floats above empty square
    Traceback (most recent call last):
    AssertionError: invalid position
    >>> print(puzzle.put_bubble(1, 1).put_boulder(2, 2).put_boulder(1, 2))
    #O..
    .O*.
    ..*.
    *.#.
    >>> puzzle.issolved()
    False
    >>> puzzle.put_bubble(3, 3)     # bubble floats below empty square
    Traceback (most recent call last):
    AssertionError: invalid position
    >>> print(puzzle.put_bubble(1, 0).put_boulder(0, 2).put_bubble(0, 3))
    #O*O
    OO*.
    ..*.
    *.#.
    >>> puzzle.issolved()
    True
    """

    def __init__(self, filename):
        self.regions = set()            # set containing all regions
        self.greens = set()             # set containing all locations of green blocks
        self.regionDict = {}            # dict mapping (r, k) -> regionName / '#'
        self.bubbleLocs = set()         # set containing all bubble locations
        self.boulderLocs = set()        # set containing all boulder locations
        with open(filename, 'r', encoding='UTF-8') as p:
            self.rows = 0
            for i, line in enumerate(p):
                line = line.strip()
                self.columns = len(line)
                self.rows += 1
                for j, c in enumerate(line):
                    self.regionDict[(i, j)] = c
                    if c != '#':
                        self.regions.add(c)
                    else:
                        self.greens.add((i,j))


    def __str__(self):
        str = ''
        for i in range(self.rows):
            for j in range(self.columns):
                if (i,j) in self.greens:
                    str += '#'
                elif (i, j) in self.bubbleLocs:
                    str += 'O'
                elif (i, j) in self.boulderLocs:
                    str += '*'
                else:
                    str += '.'
            str += '\n'
        str = str[:-1]
        return str

    def squares(self, s):
        assert s in self.regions, 'invalid region'
        area = set()
        for pos, name in self.regionDict.items():
            if name == s:
                area.add(pos)
        return area

    def bubble(self, s):
        assert s in self.regions, 'invalid region'
        for pos in self.squares(s):
            if pos in self.bubbleLocs:
                return pos
        return None

    def boulder(self, s):
        assert s in self.regions, 'invalid region'
        for pos in self.squares(s):
            if pos in self.boulderLocs:
                return pos
        return None

    def isempty(self, r, k):
        if not 0 <= r < self.rows or not 0 <= k < self.columns:
            return False
        return ((r, k) not in self.greens and
                (r, k) not in self.bubbleLocs and
                (r, k) not in self.boulderLocs)

    def put_bubble(self, r, k):
        assert self.isempty(r, k), 'invalid position'
        assert r == 0 or not self.isempty(r-1, k), 'invalid position'
        assert self.bubble(self.regionDict[(r,k)]) is None, 'invalid position'
        self.bubbleLocs.add((r,k))
        return self

    def put_boulder(self, r, k):
        assert self.isempty(r, k), 'invalid position'
        assert r == self.rows-1 or not self.isempty(r+1, k), 'invalid position'
        assert self.boulder(self.regionDict[(r,k)]) is None, 'invalid position'
        self.boulderLocs.add((r,k))
        return self

    def issolved(self):
        return len(self.boulderLocs) == len(self.bubbleLocs) == len(self.regions)







if __name__ == '__main__':
    import doctest
    doctest.testmod()











