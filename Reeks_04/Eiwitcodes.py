def isaminowoord(w):
    """
    >>> isaminowoord('ALEA')
    True
    >>> isaminowoord('iacta')
    True
    >>> isaminowoord('Proline')
    False
    """

    if len(w) < 2:
        return False

    nietAminoLetters = {'B', 'J', 'O', 'U', 'X', 'Z'}

    for letter in w.upper():
        if not letter.isalpha() or letter in nietAminoLetters:
            return False

    return True


def posities(eiwitSeq, letter):
    """
    >>> eiwit = 'HGLAVPFRTTHPSLECGRTSWARWSLDIAEFWLAWEASDCITDEDTKFQGDAVVAQM'
    >>> posities(eiwit, 'A')
    [3, 21, 28, 33, 36, 51, 54]
    >>> posities(eiwit, 'l')
    [2, 13, 25, 32]
    """

    letter = letter.upper()

    indices = []

    for idx, l in enumerate(eiwitSeq.upper()):
        if l == letter:
            indices.append(idx)

    return indices


def eiwitcode(ei, p, s, l):
    """
    >>> eiwit = 'HGLAVPFRTTHPSLECGRTSWARWSLDIAEFWLAWEASDCITDEDTKFQGDAVVAQM'
    >>> eiwitcode(eiwit, 21, 11, 4)
    'ALEA'
    >>> eiwitcode(eiwit, 27, -6, 5)
    'IACTA'
    >>> eiwitcode(eiwit, 29, 8, 3)
    'EST'
    >>> eiwitcode(eiwit, 0, 25, 6)
    ''
    """

    if not 0 <= s * (l-1) + p < len(ei):
        return ''


    code = ''

    while 0 <= p < len(ei) and len(code) < l:
        code += ei[p]
        p += s

    return code



def eiwitzoeker(seq, w, maxstap=None):
    """
    >>> eiwit = 'HGLAVPFRTTHPSLECGRTSWARWSLDIAEFWLAWEASDCITDEDTKFQGDAVVAQM'
    >>> eiwitzoeker(eiwit, 'ALEA')
    [(21, 4), (21, 11), (36, -11)]
    >>> eiwitzoeker(eiwit, 'iacta')
    [(27, -6), (27, 6)]
    >>> eiwitzoeker(eiwit, 'EST')
    [(29, -10), (29, 8)]
    >>> eiwitzoeker(eiwit, 'EST', maxstap=8)
    [(29, 8)]
    >>> eiwitzoeker(eiwit, 'Proline')
    Traceback (most recent call last):
    AssertionError: ongeldig aminowoord
    >>> eiwitzoeker('agwrdlsiivchktneaadaeineidnaeewinnnihfnigeyidmeninedanwce', 'adenine')
    [(16, 2), (52, -1)]
    """

    w = w.upper()
    seq = seq.upper()

    assert isaminowoord(w), 'ongeldig aminowoord'

    readPossibilities = []

    startPosses = posities(seq, w[0])
    secondPosses = posities(seq, w[1])

    for p1 in startPosses:
        for p2 in secondPosses:
            step = p2-p1
            if maxstap is None or abs(step) <= maxstap:
                if eiwitcode(seq, p1, step, len(w)) == w:
                    readPossibilities.append((p1, step))




    return readPossibilities




if __name__ == "__main__":
    import doctest
    doctest.testmod()