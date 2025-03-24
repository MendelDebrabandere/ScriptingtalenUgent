
class Cipher:
    """
    >>> cipher = Cipher('pokemon.txt')
    >>> cipher.name(25)
    'PIKACHU'
    >>> cipher.name(83)
    'FARFETCHD'
    >>> cipher.name(474)
    'PORYGONZ'
    >>> cipher.name(538)
    'THROH'
    >>> cipher.name(642)
    'THUNDURUS'
    >>> cipher.name(811)
    'THWACKEY'
    >>> cipher.name(828)
    'THIEVUL'
    >>> cipher.name(994)
    'IRONMOTH'
    >>> cipher.name(1111)

    >>> cipher.decode('#0828.2 #0979.2 #0382.3 #0197.1 #0460.1 #0319.3 #0932.1 #0927.1 #0025.7')
    'THANKYOUASHANDPIKACHU'

    >>> cipher.longest_prefix('Thank You Ash And Pikachu') ==  ({538, 642, 811, 828}, 2)
    True
    >>> cipher.longest_prefix('ANKYOUASHANDPIKACHU') == ({347, 979}, 2)
    True
    >>> cipher.longest_prefix('KYOUASHANDPIKACHU') == ({382}, 3)
    True

    >>> cipher.encode_prefix('Thank You Ash And Pikachu')
    (828, 2)
    >>> cipher.encode_prefix('ANKYOUASHANDPIKACHU')
    (979, 2)
    >>> cipher.encode_prefix('KYOUASHANDPIKACHU')
    (382, 3)

    >>> cipher.encode('Thank You Ash And Pikachu')
    '#0828.2 #0979.2 #0382.3 #0197.1 #0460.1 #0319.3 #0932.1 #0927.1 #0025.7'
    >>> cipher.encode('#ThankYouAshAndPikachu')
    '#0828.2 #0979.2 #0382.3 #0197.1 #0460.1 #0319.3 #0932.1 #0927.1 #0025.7'
    """


    def __init__(self, file_loc):
        self.name_to_number = {}
        self.number_to_name = {} # using a dict just in case the input isnt sorted

        with open(file_loc, 'r', encoding='UTF-8') as invoer:
            for line in invoer:
                line = line.strip().split(' ')
                number = int(line[0])
                name = ''.join(line[1:]).upper()
                name = ''.join([c.upper() for c in name if c.isalpha()])
                self.number_to_name[number] = name
                self.name_to_number[name] = number

    def name(self, ID):
        if ID in self.number_to_name:
            return self.number_to_name[ID]
        return None

    def decode(self, ciphertext):
        returnstr = ''
        for code in ciphertext.split(' '):
            length = int(code.split('.')[1])
            number = int(code.split('.')[0][1:])
            returnstr += self.name(number)[:length]
        return returnstr

    def longest_prefix(self, t):
        t = ''.join([c.upper() for c in t if c.isalpha()])
        for idx in range(len(t), 0, -1):
            pref = t[:idx].upper()
            pokemons = set()
            for name in self.name_to_number:
                if name.startswith(pref):
                    pokemons.add(name)
            if len(pokemons) != 0:
                pokemons = {self.name_to_number[pokemon] for pokemon in pokemons}
                return pokemons, idx
        return set(), 0

    def encode_prefix(self, t):
        data = self.longest_prefix(t)
        names_set = {self.name(number) for number in data[0]}
        number_with_first_name = self.name_to_number[min(names_set)]
        return number_with_first_name, data[1]

    def encode(self, t):
        t = ''.join([c.upper() for c in t if c.isalpha()])
        codes = []
        while len(t) > 0:
            code = self.encode_prefix(t)
            t = t[code[1]:]
            code = f'#{str(code[0]).rjust(4, '0')}.{code[1]}'
            codes.append(code)

        return ' '.join(codes)





if __name__ == '__main__':
    import doctest
    doctest.testmod()



