def klok(minutes):
    """
    >>> klok(0)
    '00:00'
    >>> klok(7)
    '23:53'
    >>> klok(123)
    '21:57'
    >>> klok('123')
    '21:57'
    """

    total = 24 * 60 - int(minutes)

    return f'{(total//60)%24:02}:{total%60:02}'


def verloop(verloopstr):
    """
    >>> aanpassingen = '1947 7,1949 3,1953 2,1960 7,1963 12,1968 7,1969 10,1972 12,1974 9,1980 7,1981 4,1983 3,1984 3'
    >>> doemdagklok = verloop(aanpassingen)
    >>> doemdagklok
    ((1947, '23:53'), (1949, '23:57'), (1953, '23:58'), (1960, '23:53'), (1963, '23:48'), (1968, '23:53'), (1969, '23:50'), (1972, '23:48'), (1974, '23:51'), (1980, '23:53'), (1981, '23:56'), (1983, '23:57'), (1984, '23:57'))
    """

    returnlist = []
    for datumshift in verloopstr.split(','):
        jaar, tijdshift = datumshift.split(' ')
        returnlist.append((int(jaar), klok(tijdshift)))

    return tuple(returnlist)


def dreiging(jaartal, doemdagklok):
    """
    >>> aanpassingen = '1947 7,1949 3,1953 2,1960 7,1963 12,1968 7,1969 10,1972 12,1974 9,1980 7,1981 4,1983 3,1984 3'
    >>> doemdagklok = verloop(aanpassingen)
    >>> doemdagklok
    ((1947, '23:53'), (1949, '23:57'), (1953, '23:58'), (1960, '23:53'), (1963, '23:48'), (1968, '23:53'), (1969, '23:50'), (1972, '23:48'), (1974, '23:51'), (1980, '23:53'), (1981, '23:56'), (1983, '23:57'), (1984, '23:57'))

    >>> dreiging(1974, doemdagklok)
    '23:51'
    >>> dreiging(1950, doemdagklok)
    '23:57'
    >>> dreiging(1965, doemdagklok)
    '23:48'
    """

    laatstetijd = ''
    for t in doemdagklok:
        if t[0] <= jaartal:
            laatstetijd = t[1]
        else:
            return laatstetijd

    return laatstetijd







if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)