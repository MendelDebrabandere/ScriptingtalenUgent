
class Kaart:
    """
    >>> kaart = Kaart('10♥')
    >>> kaart
    Kaart('10♥')
    >>> print(kaart)
    10♥

    >>> Kaart('1♥0')
    Traceback (most recent call last):
    AssertionError: ongeldige kaart

    >>> Kaart('2♥') < Kaart('10♥')
    True
    >>> Kaart('7♥') == Kaart('7♥')
    True
    >>> Kaart('Q♣') > Kaart('8♣')
    True
    >>> Kaart('7♥') != Kaart('7♣')
    True
    >>> Kaart('7♥') <= Kaart('7♥')
    True
    >>> Kaart('7♥') >= Kaart('7♥')
    True

    >>> Kaart('2♥') < Kaart('10♣')
    Traceback (most recent call last):
    AssertionError: kaarten van verschillende soort zijn onvergelijkbaar
    """

    rangen = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q' , 'K', 'A']

    def __init__(self, b):
        assert isinstance(b, str), 'ongeldige kaart'
        assert b[-1] in '♣♦♥♠', 'ongeldige kaart'
        assert b[:-1] in Kaart.rangen, 'ongeldige kaart'
        self.b = b

    def __str__(self):
        return self.b

    def __repr__(self):
        return f"{__class__.__name__}('{self.b}')"

    def __eq__(self, other):
        return self.b == other.b

    def __lt__(self, other):
        assert self.b[-1] == other.b[-1], 'kaarten van verschillende soort zijn onvergelijkbaar'
        return Kaart.rangen.index(self.b[:-1]) <  Kaart.rangen.index(other.b[:-1])

    def __le__(self, other):
        assert self.b[-1] == other.b[-1], 'kaarten van verschillende soort zijn onvergelijkbaar'
        return Kaart.rangen.index(self.b[:-1]) <=  Kaart.rangen.index(other.b[:-1])

    def __gt__(self, other):
        assert self.b[-1] == other.b[-1], 'kaarten van verschillende soort zijn onvergelijkbaar'
        return Kaart.rangen.index(self.b[:-1]) >  Kaart.rangen.index(other.b[:-1])

    def __ge__(self, other):
        assert self.b[-1] == other.b[-1], 'kaarten van verschillende soort zijn onvergelijkbaar'
        return Kaart.rangen.index(self.b[:-1]) >=  Kaart.rangen.index(other.b[:-1])

    def same_rank(self, other):
        return self.b[-1] == other.b[-1]

    def color(self):
        if self.b[-1] in '♦♥':
            return 'rood'
        return 'zwart'


class Hand:
    """
    >>> hand = Hand('6♣', 'K♠', '9♣', 'Q♦', 'Q♠', 'K♣', 'A♣', '4♣', '2♥', 'J♥', '4♠', '3♥', '7♠')
    >>> hand
    Hand('6♣', 'K♠', '9♣', 'Q♦', 'Q♠', 'K♣', 'A♣', '4♣', '2♥', 'J♥', '4♠', '3♥', '7♠')
    >>> print(hand)
    6♣ K♠ 9♣ Q♦ Q♠ K♣ A♣ 4♣ 2♥ J♥ 4♠ 3♥ 7♠
    >>> len(hand)
    13
    >>> hand.isgesorteerd()
    False
    >>> hand.verplaats(1, 12)
    Hand('6♣', '9♣', 'Q♦', 'Q♠', 'K♣', 'A♣', '4♣', '2♥', 'J♥', '4♠', '3♥', '7♠', 'K♠')
    >>> hand.isgesorteerd()
    False
    >>> hand.verplaats(-3, 42)
    Traceback (most recent call last):
    AssertionError: ongeldige verplaatsing
    >>> hand.verplaats(2, 12).verplaats(2, 10)
    Hand('6♣', '9♣', 'K♣', 'A♣', '4♣', '2♥', 'J♥', '4♠', '3♥', '7♠', 'Q♠', 'K♠', 'Q♦')
    >>> hand.isgesorteerd()
    False
    >>> hand.verplaats(4, 0).verplaats(8, 6)
    Hand('4♣', '6♣', '9♣', 'K♣', 'A♣', '2♥', '3♥', 'J♥', '4♠', '7♠', 'Q♠', 'K♠', 'Q♦')
    >>> hand.isgesorteerd()
    True

    >>> Hand('5♦', '4♦', 'spam', '9♥', '3♦')       # ongeldige kaart
    Traceback (most recent call last):
    AssertionError: ongeldige hand
    >>> Hand('9♥', '5♦', '4♦', '5♥', '9♥', '3♦')   # dubbele kaart: 9♥
    Traceback (most recent call last):
    AssertionError: ongeldige hand
    """

    def __init__(self, *args):
        self.cards = []
        for d in args:
            try:
                self.cards.append(Kaart(d))
            except AssertionError:
                assert False, 'ongeldige hand'

        for kaart in self.cards:
            assert self.cards.count(kaart) == 1, 'ongeldige hand'

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)

    def __repr__(self):
        return f"{__class__.__name__}('{"', '".join(str(card) for card in self.cards)}')"

    def __len__(self):
        return len(self.cards)

    def verplaats(self, i, j):
        assert 0 <= i < len(self) and 0 <= j < len(self), 'ongeldige verplaatsing'
        kaart = self.cards[i]
        self.cards.remove(kaart)
        self.cards.insert(j, kaart)
        return self

    def isgesorteerd(self):
        if len(self) == 0:
            return True

        ranks = set(self.cards[0].b[-1])
        passedRanks = [self.cards[0]]
        prevKaart = None
        for kaart in self.cards:
            if prevKaart is not None:
                if prevKaart.same_rank(kaart):
                    if prevKaart >= kaart:
                        return False
                else: # not same rank
                    if kaart.b[-1] in ranks:
                        return False
                    ranks.add(kaart.b[-1])
                    passedRanks.append(kaart)
            prevKaart = kaart

        if len(passedRanks) > 4:
            return False

        if len(passedRanks) > 2:
            for i in range(0, len(passedRanks)-1):
                if passedRanks[i].color() == passedRanks[i+1].color():
                    return False

        return True



if __name__ == '__main__':
    import doctest
    doctest.testmod()



