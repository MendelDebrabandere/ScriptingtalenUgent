def isISBN(val):

    """
    >>> isISBN('9-9715-0210-0')
    True
    >>> isISBN('997-150-210-0')
    False
    >>> isISBN('9-9715-0210-8')
    False
    """

    if not isinstance(val, str):
        return False

    groepen = val.split('-')
    if tuple(len(e) for e in groepen) != (1,4,4,1):
        return False

    code = ''.join(groepen)
    if not code[:-1].isnumeric():
        return False

    controle = sum( (i+1) * int(code[i]) for i in range(9) ) % 11 == getNum(code[-1])
    return controle


def getNum(val):
    if val == 'X':
        return 10
    else:
        return int(val)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)