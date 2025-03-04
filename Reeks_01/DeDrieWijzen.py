import math

t = float(input())
T = round(t * 100)
bigT = T * 10000


for A in range (1,150):
    for B in range(A,T):
        C = (T - A - B)
        if A * B * C == bigT:
            a = A / 100
            b = B / 100
            c = C / 100
            print(f'€{a:.2f} + €{b:.2f} + €{c:.2f} = €{a:.2f} x €{b:.2f} x €{c:.2f} = €{t:.2f}')
            exit()
