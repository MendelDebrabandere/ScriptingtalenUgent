def isveelhoek(v):
    """
    >>> isveelhoek(['DRIEHOEK', 'KEERMUUR', 'NACHTBUS'])
    True
    >>> isveelhoek(('kuisheid', 'RELATIES', 'AFREMMEN'))
    False
    >>> isveelhoek('SETPUNTEN, INKTZWART, OVERNEMER, WATERSTAD')
    False
    >>> isveelhoek(('ERONDERDOOR', 'ONTSPANNEND', 'BEGINSCHERM', 3.14, 'FAMILIEGRAF'))
    False
    """





    if len(v) < 3 or not isinstance(v, (tuple, list)) or not isinstance(v[0], str):
        return False

    stringLength = len(v[0])

    for c in v:
        if not isinstance(c, str) or c != c.upper() or len(c) != stringLength or not c.isalpha():
            return False

    return True


def oplossing(v, start=0, wijzerzin=True):
    """
    >>> oplossing(['DRIEHOEK', 'KEERMUUR', 'NACHTBUS'])
    'DECEMBER'
    >>> oplossing(('KUISHEID', 'RELATIES', 'AFREMMEN'))
    'KERSTMIS'
    >>> oplossing(['OVERNEMER', 'WATERSTAD', 'SETPUNTEN', 'INKTZWART'], start=2)
    'SNEEUWMAN'
    >>> oplossing(('DAMESROMANS', 'BEGINSCHERM', 'ONTSPANNEND', 'ERONDERDOOR', 'FAMILIEGRAF'), start=3, wijzerzin=False)
    'ENGELENHAAR'
    """

    assert isveelhoek(v), 'ongeldige veelhoek'

    woordLength = len(v[0])
    listLength = len(v)

    woord = ''

    for i in range(woordLength):
        woord += v[start][i]

        start += 1 if wijzerzin else -1
        start %= listLength


    return woord


def oplossingen(v, wijzerzin=None):
    """
    >>> oplossingen(['DRIEHOEK', 'KEERMUUR', 'NACHTBUS']) == {'DAEETUES', 'DECEMBER', 'KAIRTOUS', 'KRCRHBUK', 'NEIHMOUR', 'NREHHUUK'}
    True
    >>> oplossingen(('KUISHEID', 'RELATIES', 'AFREMMEN'), wijzerzin=True) == {'AULEHIED', 'KERSTMIS', 'RFIAMEEN'}
    True
    >>> oplossingen(['OVERNEMER', 'WATERSTAD', 'SETPUNTEN', 'INKTZWART'], wijzerzin=True) == {'IVTPZETET', 'OATTNSTRR', 'SNEEUWMAN', 'WEKRRNAED'}
    True
    >>> oplossingen(('DAMESROMANS', 'BEGINSCHERM', 'ONTSPANNEND', 'ERONDERDOOR', 'FAMILIEGRAF'), wijzerzin=False) == {'BAMNPSOGONM', 'DAOSNREDERS', 'ENGELENHAAR', 'FRTISIRNENF', 'OEMIDACMROD'}
    True
    """

    assert isveelhoek(v), 'ongeldige veelhoek'

    opl = set()

    for start in range(len(v)):
        if wijzerzin is None:
            opl.add(oplossing(v, start=start, wijzerzin=True))
            opl.add(oplossing(v, start=start, wijzerzin=False))
        else:
            opl.add(oplossing(v, start=start, wijzerzin=wijzerzin))

    return opl










if __name__ == "__main__":
    import doctest
    doctest.testmod()