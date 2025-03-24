def solveISBN(nummer):
    sum = 0
    for i in range(9):
        sum += (i+1) * int(nummer[i])
    if sum % 11 == strtonum(nummer[9]):
        print('OK')
    else:
        print('FOUT')

def strtonum(s):
    if s == 'X':
        return 10
    else:
        return int(s)



inp = input()
while inp != 'stop':
    solveISBN(inp)
    inp = input()