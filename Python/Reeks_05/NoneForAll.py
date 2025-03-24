import sys


def euclidean_distance(a, b):
    """
    >>> euclidean_distance((0, 0), (3, 4))
    5.0
    """
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


def manhattan_distance(a, b):
    """
    >>> manhattan_distance((0, 0), (3, 4))
    7.0
    """
    return float(abs(a[0]-b[0]) + abs(a[1]-b[1]))


def chessboard_distance(a, b):
    """
    >>> chessboard_distance((0, 0), (3, 4))
    4.0
    """
    return float(max(abs(a[0]-b[0]), abs(a[1]-b[1])))


def herd(fileName):
    """
    >>> herd('herd.txt') == (9, 9, {(2, 3): 'A', (0, 6): 'B', (6, 1): 'C', (4, 7): 'D', (7, 5): 'E'})
    True
    """
    with open(fileName, 'r') as invoer:
        antilopeDict = {}
        rows = 0
        for row, line in enumerate(invoer):
            line = line.strip()
            columns = len(line)
            rows += 1
            for column, char in enumerate(line):
                if char != '.':
                    antilopeDict[row, column] = char
    return rows, columns, antilopeDict


def nearest_antelope(pos, dict, distance=euclidean_distance):
    """
    >>> positions = {(2, 3): 'A', (0, 6): 'B', (6, 1): 'C', (4, 7): 'D', (7, 5): 'E'}
    >>> nearest_antelope((0, 0), positions)
    {'A'}
    >>> nearest_antelope((3, 5), positions, distance=manhattan_distance) == {'A', 'D'}
    True
    >>> nearest_antelope((2, 5), positions, distance=chessboard_distance) == {'A', 'B', 'D'}
    True
    """
    closestAntilopes = set()
    closestDist = sys.float_info.max

    for otherPos in dict:
        dist = distance(pos, otherPos)
        if dist == closestDist:
            closestAntilopes.add(dict[otherPos])
        elif dist < closestDist:
            closestDist = dist
            closestAntilopes = {dict[otherPos]}

    return closestAntilopes


def regions(fileName, distance=euclidean_distance):
    """
    >>> print(regions('herd.txt'))
    aaaabbBbb
    aaaaabbbb
    aaaAaabdd
    aaaaaaddd
    ccaaaddDd
    cccceeddd
    cCcceeedd
    ccceeEeee
    ccceeeeee
    >>> print(regions('herd.txt', distance=manhattan_distance))
    aaaabbBbb
    aaaaabbbb
    aaaAaabdd
    aaaaaaddd
    ccaaaddDd
    cccaeeddd
    cCcceeedd
    ccceeEeee
    ccceeeeee
    >>> print(regions('herd.txt', distance=chessboard_distance))
    aaaaabBbb
    aaaaabbbb
    aaaAaabbb
    aaaaaaddd
    caaaaadDd
    ccccedddd
    cCcceeedd
    cccceEeed
    cccceeeee
    """
    rows, columns, antilopes = herd(fileName)
    returnstr = ''

    for i in range(rows):
        for j in range(columns):
            if (i,j) not in antilopes:
                char = min(nearest_antelope((i,j), antilopes, distance))
                returnstr += char.lower()
            else:
                returnstr += antilopes[i,j]
        returnstr += '\n'

    return returnstr[:-1] # laatste newline weg doen







if __name__ == '__main__':
    import doctest
    doctest.testmod()