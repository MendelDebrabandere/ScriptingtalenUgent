def voorkomens(woord):
    """
    >>> voorkomens('filmproducent')
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
    >>> voorkomens('DOCTORWHO')
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
    >>> voorkomens('whiskyproducent')
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
    """

    returnList = [0] * 26

    for c in woord.lower():
        returnList[ord(c) - ord('a')] += 1

    return returnList



def isogram(woord):
    """
    >>> isogram('filmproducent')
    True
    >>> isogram('DOCTORWHO')
    False
    >>> isogram('whiskyproducent')
    True
    """

    for voorkomen in voorkomens(woord):
        if voorkomen > 1:
            return False

    return True


def anagram(woord1, woord2):
    """
    >>> anagram('DOCTORWHO', 'Torchwood')
    True
    >>> anagram('isogram', 'anagram')
    False
    >>> anagram('CENTRALISERENDE', 'decentraliseren')
    True
    """

    return voorkomens(woord1) == voorkomens(woord2)








if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)