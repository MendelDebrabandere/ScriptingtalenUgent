def decodeer(bericht):

    """
    >>> decodeer('Oea  ie.mtat n')
    'One at a time.'
    >>> decodeer("W'entwies u o,cnw ev.erse a ybtb,rta o re")
    "We're not waiters, but boy, can we serve."
    >>> decodeer('Dtn  enspae srsy oemasntigt s.uo nho ne vL.ki iryl intagia')
    'Dating a tennis player is risky. Love means nothing to us.'
    """

    if len(bericht) <= 1:
        return bericht
    return bericht[0] + bericht[-1] + decodeer(bericht[1:-1])



def codeer(bericht):

    """
    >>> codeer('One at a time.')
    'Oea  ie.mtat n'
    >>> codeer("We're not waiters, but boy, can we serve.")
    "W'entwies u o,cnw ev.erse a ybtb,rta o re"
    >>> codeer('Dating a tennis player is risky. Love means nothing to us.')
    'Dtn  enspae srsy oemasntigt s.uo nho ne vL.ki iryl intagia'
    """

    if len(bericht) <= 1:
        return bericht
    return bericht[0] + codeer(bericht[2:]) + bericht[1]



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    # codeer('One at a time.')
