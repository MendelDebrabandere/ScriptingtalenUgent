alpha = input()
n = int(input())

def prepinput(alph):
    returnstr = ''
    leadingzero = True
    for c in alph:
        if c.isnumeric():
            if leadingzero and c == '0':
                pass
            else:
                leadingzero = False
                returnstr += c
    return returnstr


alpha = prepinput(alpha)
for i in range(1,n+1):
    outp = ''
    for j in range(i):
        num = 0
        for k in range (i):
            ch = alpha[0]
            alpha = alpha[1:]
            num += int(ch)
        outp += f'{num} '
    print(outp[:-1])



