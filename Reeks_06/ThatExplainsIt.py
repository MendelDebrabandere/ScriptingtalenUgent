class Persoon:

    def __init__(self, code, naam, geslacht):
        self.code = code
        self.naam = naam
        self.geslacht = geslacht
        self.kinderen = set()
        self.ouders = set()

    def __str__(self):
        return self.naam

    def __repr__(self):
        return f"{__class__.__name__}('{self.code}', '{self.naam}', '{self.geslacht}')"


class Stamboom:
    """
    >>> got = Stamboom('personen.got.txt', 'relaties.got.txt')
    >>> got_CB = got.persoon('CB')
    >>> got_CB
    Persoon('CB', 'Alannys Harlaw', 'V')
    >>> got.nakomelingen(got_CB)
    {Persoon('BX', 'Rodrik Greyjoy', 'M'), Persoon('CA', 'Theon Greyjoy', 'M'), Persoon('BY', 'Maron Greyjoy', 'M'), Persoon('BZ', 'Asha Greyjoy', 'V')}
    """

    def __init__(self, personen_file, relaties_file):
        self.personen = {}
        with open(personen_file, 'r', encoding='UTF-8') as p_file:
            for line in p_file:
                line = line.strip().split(' ')
                self.personen[line[0]] = (Persoon(line[0], ' '.join(line[2:-1]), line[-1][1]))

        with open(relaties_file, 'r', encoding='UTF-8') as r_file:
            for line in r_file:
                line = line.strip().split(',')
                if len(line[-1]) == 0:
                    line = line[:-1]
                for relatie in line:
                    relatie = relatie.strip().split('->')
                    relatie[0] = relatie[0].strip()
                    relatie[1] = relatie[1].strip()
                    self.personen[relatie[1].strip()].ouders.add(relatie[0])
                    self.personen[relatie[0]].kinderen.add(relatie[1])

    def persoon(self, c):
        assert c in self.personen, 'onbekende persoon'
        return self.personen[c]

    def ouders(self, p):
        for persoon in self.personen:
            if persoon == p.code:
                return_set = set()
                for code in self.personen[persoon].ouders:
                    return_set.add(self.personen[code])
                return return_set
        return set()

    def vader(self, p):
        for persoon in self.ouders(p):
            if persoon.geslacht == 'M':
                return persoon
        return None

    def moeder(self, p):
        for persoon in self.ouders(p):
            if persoon.geslacht == 'V':
                return persoon
        return None

    def kinderen(self, p):
        for persoon in self.personen:
            if persoon == p.code:
                return_set = set()
                for code in self.personen[persoon].kinderen:
                    return_set.add(self.personen[code])
                return return_set
        return set()

    def zonen(self, p):
        return_set = set()
        for persoon in self.kinderen(p):
            if persoon.geslacht == 'M':
                return_set.add(persoon)
        return return_set

    def dochters(self, p):
        return_set = set()
        for persoon in self.kinderen(p):
            if persoon.geslacht == 'V':
                return_set.add(persoon)
        return return_set

    def broers(self, p):
        return_set = set()
        for ouder in self.ouders(p):
            return_set = return_set.union(self.zonen(ouder))
        return_set.discard(p)
        return return_set

    def zussen(self, p):
        return_set = set()
        for ouder in self.ouders(p):
            return_set = return_set.union(self.dochters(ouder))
        return_set.discard(p)
        return return_set

    def nonkels(self, p):
        return_set = set()
        for ouder in self.ouders(p):
            return_set = return_set.union(self.broers(ouder))
        return return_set

    def tantes(self, p):
        return_set = set()
        for ouder in self.ouders(p):
            return_set = return_set.union(self.zussen(ouder))
        return return_set

    def voorouders(self, p, return_set=None):
        if return_set is None:
            return_set = set()

        for ouder in self.ouders(p):
            return_set.add(ouder)
            self.voorouders(ouder, return_set)

        return return_set

    def nakomelingen(self, p, return_set=None):
        if return_set is None:
            return_set = set()

        for kind in self.kinderen(p):
            return_set.add(kind)
            self.nakomelingen(kind, return_set)

        return return_set

