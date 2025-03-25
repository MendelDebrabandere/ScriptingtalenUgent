class Substitutie:
    """
    >>> substitutie1 = Substitutie('MANYREQUSTHVBCIDFOLWGZXPKJ')
    >>> substitutie1.codeer("Why, if 'tis dancing you would be,")
    "Xuk, se 'wsl ymcnscq kig xigvy ar,"
    >>> substitutie1.decodeer("Xuk, se 'wsl ymcnscq kig xigvy ar,")
    "Why, if 'tis dancing you would be,"

    >>> substitutie2 = Substitutie('JHAZTENYXMLOCUFBQVKPSGWRDI')
    >>> substitutie2.codeer("Why, if 'tis dancing you would be,")
    "Wyd, xe 'pxk zjuaxun dfs wfsoz ht,"
    >>> substitutie2.decodeer("Wyd, xe 'pxk zjuaxun dfs wfsoz ht,")
    "Why, if 'tis dancing you would be,"

    >>> Substitutie('abcdefghijklmnopqrstuvwyz')     # letter x ontbreekt
    Traceback (most recent call last):
    AssertionError: ongeldige sleutel
    >>> Substitutie('abcdefghijklmnopqrstuvwxyza')   # letter a komt twee keer voor
    Traceback (most recent call last):
    AssertionError: ongeldige sleutel
    """

    def __init__(self, sleutel):
        self.sleutel = sleutel.upper()

        assert len(self.sleutel) == 26, 'ongeldige sleutel'
        for i in range(26):
            assert chr(i + ord('A')) in self.sleutel, 'ongeldige sleutel'


    def codeer(self, tekst):
        gecodeerd = ''

        for c in tekst:
            if c.isalpha():
                c_idx = ord(c.upper()) - ord('A')
                c_coded = self.sleutel[c_idx]
                if c.islower():
                    c_coded = c_coded.lower()
                gecodeerd += c_coded
            else:
                gecodeerd += c

        return gecodeerd


    def decodeer(self, cijfertekst):
        klaretekst = ''

        for c in cijfertekst:
            if c.isalpha():
                c_idx = self.sleutel.index(c.upper())
                c_klaar = chr(ord('A') + c_idx)
                if c.islower():
                    c_klaar = c_klaar.lower()
                klaretekst += c_klaar
            else:
                klaretekst += c

        return klaretekst





class Olum:
    """
    >>> cijfer = Olum('MANYREQUSTHVBCIDFOLWGZXPKJ', 'JHAZTENYXMLOCUFBQVKPSGWRDI')
    >>> cijfer.codeer_regel("Why, if 'tis dancing you would be,")
    'XUKEXWSLZJUAXUNKIGWFSOZRA'
    >>> cijfer.codeer_regel('There is brisker pipes than poetry.')
    'WURORKXAOSLHROBXBTKCMUWDVPTFB'
    >>> cijfer.codeer('houseman1896.txt')
    XUKEXWSLZJUAXUNKIGWFSOZRAWURORKXAOSLHROB
    XBTKCMUWDVPTFBLMKEFVWMUXTVTWUIDDJVZKBRMC
    WOIWYDXMLUFPVSHAGSVWUFWORCWUIDUJCMVTTBEI
    TUNOJUZAORXLORSVRZSVVFSQXOCMUWPYTRLGBMCY
    POJCLRIYTVFCCMUWUFPOXCNMCIWMSKPXEDQIYKLK
    MXFPBMCMVRCJUMVRKWURKPSEEIWZVXULEIOETOOF
    WKBIUXPXUGOWLFPWUSCH
    >>> cijfer.codeer('houseman1896.txt', 'feynman_cipher_#2.txt')
    >>> cijfer.codeer('feynman1953.txt', breedte=33)
    WURVFXGJYTHEIZXSQXOBGSVRUDOOJXATB
    KTARVIXPYTMYABMVUFXPXKUJVPLSDVTGN
    GOSIGLWURPKFCVGELLRNNGLPYTFVTPXAJ
    OSCWRODORWMWSICLFKEMOTGJYCRRAOJVN
    TODVMNSQIVICRBICRUDCSKXYPDMDROJUZ
    ICRVFWXIFPXIVVIEPYTDOIAVRBOOXWRAK
    PSZXTZKVROSWCRCFVEESOLWKTOBXAUXVB
    >>> cijfer.codeer('feynman1953.txt', 'feynman_cipher_#3.txt', breedte=33)

    >>> Olum('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwyz')     # letter x ontbreekt in tweede sleutel
    Traceback (most recent call last):
    AssertionError: ongeldige sleutel
    >>> Olum('abcdefghijklmnopqrstuvwxyza', 'abcdefghijklmnopqrstuvwxyz')   # letter a komt 2× voor in eerste sleutel
    Traceback (most recent call last):
    AssertionError: ongeldige sleutel
    """


    def __init__(self, sleutel1, sleutel2):
        self.sub1 = Substitutie(sleutel1)
        self.sub2 = Substitutie(sleutel2)

    # helper functie voor mezelf
    # anders is dit stukje code 2 keer gedupliceert in codeer_regel()
    def codeer_woord(self, curr_woord, woord_counter):
        woord_gecodeerd = ''
        if woord_counter % 2 == 0:
            woord_gecodeerd = self.sub1.codeer(curr_woord)
        else:
            woord_gecodeerd = self.sub2.codeer(curr_woord)
        if len(woord_gecodeerd) % 2 == 0:
            woord_gecodeerd = woord_gecodeerd[::-1]
        return woord_gecodeerd


    def codeer_regel(self, regel):
        gecodeerd = ''

        curr_woord = ''
        woord_counter = 0

        for c in regel:
            if c.isalpha():
                curr_woord += c
            else:
                if len(curr_woord) > 0:
                    gecodeerd += self.codeer_woord(curr_woord, woord_counter)
                    woord_counter += 1
                    curr_woord = ''

        if len(curr_woord) > 0: # if line didnt end with newline, the loop can end with still stuff in curr_woord
            gecodeerd += self.codeer_woord(curr_woord, woord_counter)

        return gecodeerd.upper()


    def codeer(self, input_file, output_file=None, breedte=40):
        gecodeerd = ''

        with open(input_file, 'r', encoding='UTF-8') as invoer:
            for line in invoer:
                gecodeerd += self.codeer_regel(line)


        lines = []
        for i in range(0, len(gecodeerd), breedte):
            lines.append(gecodeerd[i:i + breedte])

        if output_file is not None:
            with open(output_file, 'w', encoding='UTF-8') as uitvoer:
                print('\n'.join(lines), file=uitvoer)
        else:
            print('\n'.join(lines))





if __name__ == '__main__':
    import doctest
    doctest.testmod()