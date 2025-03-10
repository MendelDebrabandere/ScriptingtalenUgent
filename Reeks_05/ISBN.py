from urllib.request import urlopen
import xml.etree.ElementTree as ET

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



def display_book_info(ISBNstring):
    """
    >>> display_book_info('9780136110675')
    Title: The Practice of Computing using Python
    Authors: William F Punch, Richard Enbody
    Publisher: Addison Wesley
    >>> display_book_info('9780136110678')
    Wrong ISBN-13 code
    """


    # check of het wel een isbn13 code is
    if not isISBN(ISBNstring):
        print('Wrong ISBN-13 code')
        return

    # get file from internet
    url = 'https://pythia.ugent.be/pythia-share/exercises/isbn9/books.php?isbn={}'
    with urlopen(url.format(ISBNstring)) as file:
        # parse xml
        tree = ET.parse(file)
        root = tree.getroot()

        # get data
        title = root.find(".//Title").text
        authors = root.find(".//AuthorsText").text
        publisher = root.find(".//PublisherText").text

        print("Title:", title)
        print("Authors:", authors.strip(' ').strip(','))
        print("Publisher:", publisher)















if __name__ == '__main__':
    import doctest
    doctest.testmod()









