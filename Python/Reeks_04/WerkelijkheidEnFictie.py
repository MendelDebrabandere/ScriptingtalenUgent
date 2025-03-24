def codeer_letter(*letters):
    """
    >>> codeer_letter('H')
    'H'
    >>> codeer_letter('e', 'H')
    'l'
    >>> codeer_letter('W', 'y')
    'U'
    """

    som = sum(ord(letter.lower()) - ord('a') for letter in letters) % 26

    checkchar = ord('A') if letters[0].isupper() else ord('a')
    return chr(som + checkchar)



def decodeer_letter(letter, diff='A'):
    """
    >>> decodeer_letter('H')
    'H'
    >>> decodeer_letter('l', 'H')
    'e'
    >>> decodeer_letter('U', 'p')
    'F'
    """

    som = (ord(letter.lower()) - ord(diff.lower())) % 26

    checkchar = ord('A') if letter.isupper() else ord('a')
    return chr(som + checkchar)



def codeer(s):
    """
    >>> codeer('Henry Walton Jones Jr.')
    'Hlrep Uwlehb Wxbrw Ba.'
    """

    gecodeerd = []

    previous_c = 'a'
    for c in s:
        if c.isalpha():
            gecodeerd.append(codeer_letter(c, previous_c))
            previous_c = c
        else:
            gecodeerd.append(c)

    return ''.join(gecodeerd)



def decodeer(s):
    """
    >>> decodeer('Hlrep Uwlehb Wxbrw Ba.')
    'Henry Walton Jones Jr.'
    """

    gecodeerd = []

    previous_c = 'a'
    for c in s:
        if c.isalpha():
            decodeerdeLetter = decodeer_letter(c, previous_c)
            gecodeerd.append(decodeerdeLetter)
            previous_c = decodeerdeLetter
        else:
            gecodeerd.append(c)

    return ''.join(gecodeerd)




if __name__ == '__main__':
    import doctest
    doctest.testmod()