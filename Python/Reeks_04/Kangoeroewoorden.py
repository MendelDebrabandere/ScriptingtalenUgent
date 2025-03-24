def kangoeroe(k, j):
    """
    >>> kangoeroe('blossom', 'bloom')
    True
    >>> kangoeroe('DISAPPOINTED', 'SAD')
    True
    >>> kangoeroe('GIGANTIC', 'giant')
    True
    >>> kangoeroe('ALONE', 'lone')
    True
    >>> kangoeroe('Marsupial', 'Kangaroo')
    False
    """

    j = j.upper()
    k = k.upper()

    kIdx = 0

    for c in j:
        kIdx = k.find(c, kIdx)
        if kIdx == -1:
            return False

    return True





def jongen(k, col):
    """
    >>> jongen('blossom', ['bloom', 'bud', 'floweret'])
    {'bloom'}
    >>> jongen('DISAPPOINTED', ('SAD', 'DOWN', 'UPSET', 'FOILED'))
    {'SAD'}
    >>> jongen('GIGANTIC', {'giant', 'colossal', 'huge', 'massive', 'enormous', 'immense', 'vast'})
    {'giant'}
    >>> jongen('ALONE', {'lone', 'one', 'only', 'solo', 'unaccompanied'})
    {'lone', 'one'}
    >>> jongen('Marsupial', ['Kangaroo', 'Wallaby', 'Koala', 'Opossum', 'Wombat'])
    set()
    """

    children = set()

    for w in col:
        if kangoeroe(k, w):
            children.add(w)

    return children

























if __name__ == "__main__":
    import doctest
    doctest.testmod()

