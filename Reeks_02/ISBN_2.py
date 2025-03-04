
def isISBN(code):
    """
    Geeft True terug als het argument een string is die een geldige ISBN-10 code
    bevat. Anders wordt False teruggegeven.

    >>> isISBN('9971502100')
    True
    >>> isISBN('9971502108')
    False
    >>> isISBN('53WKEFF2C')
    False
    >>> isISBN(4378580136)
    False
    """
    if type(code) is int or not code[:-1].isnumeric():
        return False
    som = 0
    for i in range(9):
        som += (i+1) * int(code[i])
    if som % 11 == tonum(code[9]):
        return True
    return False





def tonum(x):
    if x == 'X':
        return 10
    return int(x)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
