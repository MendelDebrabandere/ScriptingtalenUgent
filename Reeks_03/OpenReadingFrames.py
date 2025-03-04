def ORFs(dna, startcodons, stopcodons):
    """
    >>> ORFs('gcccttaattttattcattggattccattcattaacgtgctgatgtcccatttgttta', ['att', 'gca', 'gcc'], ['tct', 'tga', 'ttt'])
    [(0, 11, 1), (7, 42, 2), (12, 56, 1), (26, 52, 3)]
    >>> ORFs('cgtgtgcacaactcaccccgtagacccaaaatgtggataacatg', ['aca', 'gtg'], ['aaa', 'ccc', 'gac'])
    [(1, 18, 2), (3, 17, 1)]
    >>> ORFs('cgagggctctcactgggacggcagaggctagtcacagtat', ['agt'], ['gac', 'ggc'])
    []
    """

    returnlijst = []

    for frame in range(1,4):

        inORF = False
        startframe = 0
        for i in range(frame-1, len(dna), 3):
            if not inORF and dna[i:i+3] in startcodons:
                startframe = i
                inORF = True
            elif inORF and dna[i:i+3] in stopcodons:
                inORF = False
                returnlijst.append(tuple((startframe, i+2, frame)))

    return ORFsort(returnlijst)


def ORFsort(lijst):

    returnlijst = []

    while lijst:    # is not empty
        smalleststartframeidx = -1
        for i, item in enumerate(lijst):
            if smalleststartframeidx == -1 or item[0] < lijst[smalleststartframeidx][0]:
                smalleststartframeidx = i
        returnlijst.append(lijst.pop(smalleststartframeidx))

    return returnlijst




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

