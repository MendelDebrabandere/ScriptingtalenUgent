
def leet2letter(file):
    """
    >>> hex2letter = leet2letter('leet.txt')
    >>> hex2letter == {'0': {'O'}, '1': {'I'}, '2': {'Z', 'R'}, '3': {'E'}, '5': {'S'}, '6': {'G'}, '7': {'L', 'Y', 'T'}, '9': {'P'}}
    True
    """

    leetDict = {}

    with open(file, 'r') as inputFile:
        for line in inputFile:
            lineValues = line.split('<->')
            valueSet = { c.upper() for c in lineValues[1].strip() }
            leetDict[lineValues[0].strip().upper()] = valueSet

    return leetDict


def letter2leet(leetDict):
    """
    >>> hex2letter = leet2letter('leet.txt')
    >>> letter2hex = letter2leet(hex2letter)
    >>> letter2hex == {'O': '0', 'I': '1', 'Z': '2', 'R': '2', 'E': '3', 'S': '5', 'G': '6', 'L': '7', 'Y': '7', 'T': '7', 'P': '9'}
    True
    """

    reverseDict = {}

    for leet, letter in leetDict.items():
        for char in letter:
            reverseDict[char.upper()] = leet

    return reverseDict


def leetspeak(name, leetDict):
    """
    >>> hex2letter = leet2letter('leet.txt')
    >>> letter2hex = letter2leet(hex2letter)
    >>> leetspeak('BADASS', letter2hex)
    'BADA55'
    >>> leetspeak('fbi', letter2hex)
    'FB1'
    >>> leetspeak('SHRUBBERY', letter2hex)
    '5H2UBB327'
    >>> leetspeak('REBECCA', letter2hex)
    '23B3CCA'
    """

    returnstr = ''

    for letter in name.upper():
        returnstr += leetDict.get(letter, letter)

    return returnstr


def ishexcolor(color):
    """
    >>> ishexcolor('#BADA55')
    True
    >>> ishexcolor('#fb1')
    True
    >>> ishexcolor('#5H2UBB327')
    False
    >>> ishexcolor('#663399')
    True
    """

    if color[0] != '#':
        return False

    if len(color) != 4 and len(color) != 7:
        return False

    for c in color[1:].upper():
        if not c.isdigit() and not ord('A') <= ord(c) <= ord('F'):
            return False

    return True


def color(name, leetDict):
    """
    >>> hex2letter = leet2letter('leet.txt')
    >>> letter2hex = letter2leet(hex2letter)
    >>> color('BADASS', letter2hex)
    '#BADA55'
    >>> color('fbi', letter2hex)
    '#FB1'
    >>> color('SHRUBBERY', letter2hex)
    Traceback (most recent call last):
    AssertionError: invalid color
    >>> color('REBECCA', letter2hex)
    Traceback (most recent call last):
    AssertionError: invalid color
    """

    code = '#' + leetspeak(name, leetDict)

    assert ishexcolor(code), 'invalid color'

    return code







if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)