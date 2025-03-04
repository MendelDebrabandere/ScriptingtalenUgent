def isISBN(code):
    """
    >>> isISBN('9789027439642')
    True
    """

    if len(code) != 13 or code[:3] not in {'978' , '979'}:
        return False

    o = sum(int(i) for i in code[:-1:2])
    e = sum(int(i) for i in code[1:-1:2])

    return int(code[-1]) == (10 - (o + 3*e) % 10) % 10



def overzicht(codes):
    """
    >>> codes = [
    ...    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
    ...    '9780817481461', '9785130738708', '9798810365062', '9795345206033',
    ...    '9792361848797', '9785197570819', '9786922535370', '9791978044523',
    ...    '9796357284378', '9792982208529', '9793509549576', '9787954527409',
    ...    '9797566046955', '9785239955499', '9787769276051', '9789910855708',
    ...    '9783807934891', '9788337967876', '9786509441823', '9795400240705',
    ...    '9787509152157', '9791478081103', '9780488170969', '9795755809220',
    ...    '9793546666847', '9792322242176', '9782582638543', '9795919445653',
    ...    '9796783939729', '9782384928398', '9787590220100', '9797422143460',
    ...    '9798853923096', '9784177414990', '9799562126426', '9794732912038',
    ...    '9787184435972', '9794455619207', '9794270312172', '9783811648340',
    ...    '9799376073039', '9798552650309', '9798485624965', '9780734764010',
    ...    '9783635963865', '9783246924279', '9797449285853', '9781631746260',
    ...    '9791853742292', '9781796458336', '9791260591924', '9789367398012'
    ... ]
    >>> overzicht(codes)
    Engelstalige landen: 8
    Franstalige landen: 4
    Duitstalige landen: 6
    Japan: 3
    Russischtalige landen: 7
    China: 8
    Overige landen: 11
    Fouten: 9
    """

    landcodes = {0:'engels', 1:'engels', 2:'frans', 3:'duits', 4:'japan', 5:'russisch', 7:'china', 6:'overig', 8:'overig', 9:'overig'}
    landen = {'engels':0, 'frans':0, 'duits':0, 'japan':0, 'russisch':0, 'china':0, 'overig':0, 'error':0}

    for code in codes:
        if not isISBN(code):
            landen['error'] += 1
        else:
            landen[landcodes[int(code[3])]] += 1

    print(f'Engelstalige landen: {landen['engels']}')
    print(f'Franstalige landen: {landen['frans']}')
    print(f'Duitstalige landen: {landen['duits']}')
    print(f'Japan: {landen['japan']}')
    print(f'Russischtalige landen: {landen['russisch']}')
    print(f'China: {landen['china']}')
    print(f'Overige landen: {landen['overig']}')
    print(f'Fouten: {landen['error']}')


















if __name__ == "__main__":
    import doctest
    doctest.testmod()