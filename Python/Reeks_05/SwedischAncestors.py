import textwrap
import itertools

def family_members(filename):
    """
    >>> relationships = family_members('data.txt')
    >>> relationships['Sincere'] == {'father': 'Jovanni', 'mother': 'Rosa'}
    True
    >>> relationships['August'] == {'father': 'Ronan', 'mother': 'Alana', 'children': {'Eric', 'Drake', 'Jadon', 'Rosa'}}
    True
    >>> relationships['Ronan'] == {'children': {'Beatrice', 'August'}}
    True
    """

    treeDict = {}

    with open(filename, 'r') as invoer:
        for line in invoer:
            lineInfo = line.strip().split(' ') # turn line into a list of names
            treeDict[lineInfo[0]] = treeDict.get(lineInfo[0], {}) # initialize mom's dict if it was not initialized yet
            treeDict[lineInfo[1]] = treeDict.get(lineInfo[1], {}) # initialize dad's dict if it was not initialized yet

            # set parent's children in treeDict
            childrenSet = {lineInfo[i] for i in range(2, len(lineInfo))}
            treeDict[lineInfo[0]]['children'] = childrenSet
            treeDict[lineInfo[1]]['children'] = childrenSet

            # add children to treeDict
            for i in range(2, len(lineInfo)):
                treeDict[lineInfo[i]] = treeDict.get(lineInfo[i], {}) # if not initialized, put a dict there
                treeDict[lineInfo[i]]['father'] = lineInfo[1] # set dad
                treeDict[lineInfo[i]]['mother'] = lineInfo[0] # set mom

    return treeDict



def ancestor(name, desc, dict):
    """
    >>> relationships = family_members('data.txt')
    >>> ancestor('Drake', 'mor', relationships)
    'Amira'
    >>> ancestor('Rosa', 'farmor', relationships)
    'Alana'
    >>> ancestor('Sincere', 'morfarfar', relationships)
    'Ronan'
    >>> ancestor('Luciana', 'morfarmor', relationships)
    Traceback (most recent call last):
    AssertionError: unknown ancestor
    """

    desc = textwrap.wrap(desc, 3)

    ancestorName = name

    for instruction in desc:
        ancestorName = dict[ancestorName].get('father' if instruction == 'far' else 'mother')
        assert ancestorName is not None, 'unknown ancestor'

    return ancestorName


def descendants(name, n, dict):
    """
    >>> relationships = family_members('data.txt')
    >>> descendants('Ronan', 1, relationships) == {'far': {'Beatrice', 'August'}}
    True
    >>> descendants('Ronan', 2, relationships) == {'morfar': {'Regan', 'Ramiro'}, 'farfar': {'Rosa', 'Eric', 'Jadon', 'Drake'}}
    True
    >>> descendants('Ronan', 3, relationships) == {'farmorfar': {'Carlos', 'Luciana', 'Ciara'}, 'farfarfar': {'Gavyn', 'Cadence', 'Aryana'}, 'mormorfar': {'Alberto', 'Natalee'}, 'morfarfar': {'Kole', 'Emmy', 'Sincere', 'Xzavier', 'Gabriella'}}
    True
    """

    descDict = {}
    possibleKeys = list(itertools.product(['far', 'mor'], repeat=n))

    for key in possibleKeys:
        key = ''.join(key)
        keySet = set()
        for child in dict:
            try:
                if ancestor(child, key, dict) == name:
                    keySet.add(child)
            except AssertionError:
                pass
        if len(keySet) != 0:
            descDict[key] = keySet

    return descDict






if __name__ == '__main__':
    import doctest
    doctest.testmod()

