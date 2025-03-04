inp = input()

returnstr = ''

alternator = False
for c in inp:

    if c.isalpha():
        alternator = not alternator
        if alternator:
            returnstr += c
    else:
        returnstr += c



print(returnstr)