
class YinYang:
    """
    >>> puzzel = YinYang(dimensie=6, wit=[(2, 0), (1, 2), (3, 2), (5, 5)], zwart=[(2, 1), (2, 4), (3, 1), (4, 1), (4, 3), (5, 0)])
    >>> print(puzzel)
    ------
    --W---
    WB--B-
    -BW---
    -B-B--
    B----W
    >>> print(puzzel.maak_wit((0, 0)))
    w-----
    --W---
    WB--B-
    -BW---
    -B-B--
    B----W
    >>> puzzel.maak_zwart((3, 2))     # positie is reeds bezet
    Traceback (most recent call last):
    AssertionError: ongeldige actie
    >>> puzzel.maak_zwart((1, 6))     # positie ligt buiten puzzel
    Traceback (most recent call last):
    AssertionError: ongeldige actie
    >>> print(puzzel.maak_zwart((5, 1)))
    w-----
    --W---
    WB--B-
    -BW---
    -B-B--
    Bb---W
    >>> puzzel.maak_zwart((4, 0))       # er wordt een vierkant gevormd
    Traceback (most recent call last):
    AssertionError: ongeldige actie
    >>> print(puzzel.maak_wit((0, 1)).maak_wit((0, 2)).maak_wit((0, 3)).maak_wit((0, 4)).maak_zwart((0, 5)))
    wwwwwb
    --W---
    WB--B-
    -BW---
    -B-B--
    Bb---W
    >>> print(puzzel.maak_leeg((0, 5)))
    wwwww-
    --W---
    WB--B-
    -BW---
    -B-B--
    Bb---W
    >>> print(puzzel.maak_wit((0, 5)))
    wwwwww
    --W---
    WB--B-
    -BW---
    -B-B--
    Bb---W
    >>> print(puzzel.maak_wit((1, 0)).maak_zwart((1, 1)).maak_zwart((1, 3)).maak_zwart((1, 4)).maak_wit((1, 5)))
    wwwwww
    wbWbbw
    WB--B-
    -BW---
    -B-B--
    Bb---W
    >>> print(puzzel.maak_wit((2, 2)).maak_wit((2, 3)).maak_wit((2, 5)))
    wwwwww
    wbWbbw
    WBwwBw
    -BW---
    -B-B--
    Bb---W
    >>> print(puzzel.maak_wit((3, 0)).maak_zwart((3, 3)).maak_zwart((3, 4)).maak_wit((3, 5)))
    wwwwww
    wbWbbw
    WBwwBw
    wBWbbw
    -B-B--
    Bb---W
    >>> print(puzzel.maak_wit((4, 0)).maak_wit((4, 2)).maak_wit((4, 4)).maak_wit((4, 5)))
    wwwwww
    wbWbbw
    WBwwBw
    wBWbbw
    wBwBww
    Bb---W
    >>> puzzel.isopgelost()
    False
    >>> print(puzzel.maak_wit((5, 2)).maak_zwart((5, 3)).maak_zwart((5, 4)))
    wwwwww
    wbWbbw
    WBwwBw
    wBWbbw
    wBwBww
    BbwbbW
    >>> puzzel.aaneengesloten_gebied((2, 1))
    {(2, 1), (3, 1), (1, 1), (5, 1), (5, 0), (4, 1)}
    >>> puzzel.aaneengesloten_gebied((3, 2))
    {(4, 0), (0, 2), (0, 5), (2, 2), (1, 0), (2, 5), (4, 2), (3, 0), (4, 5), (0, 1), (1, 2), (0, 4), (1, 5), (3, 2), (3, 5), (5, 2), (4, 4), (5, 5), (0, 0), (0, 3), (2, 0), (2, 3)}
    >>> puzzel.isopgelost()
    False
    >>> print(puzzel.maak_leeg((5, 2)).maak_zwart((5, 2)))
    wwwwww
    wbWbbw
    WBwwBw
    wBWbbw
    wBwBww
    BbbbbW
    >>> puzzel.aaneengesloten_gebied((2, 1))
    {(1, 3), (2, 4), (2, 1), (3, 4), (4, 3), (3, 1), (1, 1), (5, 4), (5, 1), (1, 4), (3, 3), (5, 0), (5, 3), (4, 1), (5, 2)}
    >>> puzzel.aaneengesloten_gebied((3, 2))
    {(4, 0), (0, 2), (0, 5), (2, 2), (1, 0), (2, 5), (4, 2), (3, 0), (4, 5), (0, 1), (1, 2), (0, 4), (1, 5), (3, 2), (3, 5), (4, 4), (5, 5), (0, 0), (0, 3), (2, 0), (2, 3)}
    >>> puzzel.isopgelost()
    True
    """

    def __init__(self, dimensie, wit, zwart):
        self.n = dimensie
        self.wit = set(wit)
        self.zwart = set(zwart)
        self.new_wit = set()   # bijhouden welke nieuw zijn toegevoegd
        self.new_zwart = set() ##

        error_message = 'ongeldige puzzel'

        for pos in wit:
            assert pos not in zwart, error_message
            assert 0 <= pos[0] < self.n and 0 <= pos[1] < self.n, error_message
            self.check_voor_vierkant(True, pos, error_message)

        for pos in zwart:
            assert 0 <= pos[0] < self.n and 0 <= pos[1] < self.n, error_message
            self.check_voor_vierkant(False, pos, error_message)


    # helper functie voor duplicatie van code te vermijden
    def check_voor_vierkant(self, is_wit, pos, error_message, p_to_delete=None):
        verzameling =  self.wit if is_wit else self.zwart
        if { pos, (pos[0]+1, pos[1]), (pos[0], pos[1]+1), (pos[0]+1, pos[1]+1) }.issubset(verzameling):
            if p_to_delete is not None:
                verzameling.remove(p_to_delete)
            assert False, error_message


    def maak_wit(self, p):
        error_message = 'ongeldige actie'
        assert 0 <= p[0] < self.n and 0 <= p[1] < self.n, error_message
        assert p not in self.wit and p not in self.zwart, error_message

        self.wit.add(p)
        # als dit faalt dan zorgt de check zelf ervoor om het punt terug te verwijderen
        self.check_voor_vierkant(True, (p[0]-1, p[1]-1), error_message, p)
        self.check_voor_vierkant(True, (p[0]-1, p[1]), error_message, p)
        self.check_voor_vierkant(True, (p[0], p[1]-1), error_message, p)
        self.check_voor_vierkant(True, (p[0], p[1]), error_message, p)

        self.new_wit.add(p)
        return self


    def maak_zwart(self, p):
        error_message = 'ongeldige actie'
        assert 0 <= p[0] < self.n and 0 <= p[1] < self.n, error_message
        assert p not in self.wit and p not in self.zwart, error_message

        self.zwart.add(p)
        # als dit faalt dan zorgt de check zelf ervoor om het punt terug te verwijderen
        self.check_voor_vierkant(False, (p[0]-1, p[1]-1), error_message, p)
        self.check_voor_vierkant(False, (p[0]-1, p[1]), error_message, p)
        self.check_voor_vierkant(False, (p[0], p[1]-1), error_message, p)
        self.check_voor_vierkant(False, (p[0], p[1]), error_message, p)

        self.new_zwart.add(p)
        return self

    def maak_leeg(self, p):
        error_message = 'ongeldige actie'
        assert 0 <= p[0] < self.n and 0 <= p[1] < self.n, error_message
        assert p in self.wit or p in self.zwart, error_message

        if p in self.new_wit:
            self.wit.remove(p)
            self.new_wit.remove(p)
        else:
            self.zwart.remove(p)
            self.new_zwart.remove(p)
        return self


    def aaneengesloten_gebied(self, p):
        if not (0 <= p[0] < self.n and 0 <= p[1] < self.n) or not (p in self.wit or p in self.zwart):
            return set()
        # flood fill
        G = {p}
        T = {p}
        verzameling = self.wit if p in self.wit else self.zwart
        while len(T) > 0:
            t = T.pop() # verwijder en get
            neighbors = {(t[0]-1, t[1]), (t[0]+1, t[1]), (t[0], t[1]-1), (t[0], t[1]+1)}
            for b in neighbors:
                if b not in G and (b in verzameling):
                    T.add(b)
                    G.add(b)
        return G


    def isopgelost(self):
        # check of alles opgevuld is en of er geen vierkanten zijn
        for r in range(self.n):
            for k in range(self.n):
                if ((r,k) not in self.wit) and ((r,k) not in self.zwart):
                    return False
                try:
                    self.check_voor_vierkant((r,k) in self.wit, (r,k), 'vierkant gespot')
                except AssertionError:
                    return False

        # check of alles in 2 aaaneengesloten gebieden zit
        wit_element = next(iter(self.wit))
        zwart_element = next(iter(self.zwart))
        if len(self.aaneengesloten_gebied(wit_element)) + len(self.aaneengesloten_gebied(zwart_element)) != self.n**2:
            return False

        return True


    def __str__(self):
        returnstr = ''
        for r in range(self.n):
            for k in range(self.n):
                if (r, k) in self.new_wit:
                    returnstr += 'w'
                elif (r, k) in self.new_zwart:
                    returnstr += 'b'
                elif (r, k) in self.wit:
                    returnstr += 'W'
                elif (r, k) in self.zwart:
                    returnstr += 'B'
                else:
                    returnstr += '-'
            returnstr += '\n'
        return returnstr[:-1]









if __name__ == '__main__':
    import doctest
    doctest.testmod()













