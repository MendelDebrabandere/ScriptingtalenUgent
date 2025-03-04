def camachoterm(n, p):
    n = str(n)

    som = 0
    for c in n:
        som += int(c)**p
    return som

def camachosom(n):
    n = str(n)

    som = 0
    for i in range(len(n)):
        som += camachoterm(n, i+1)
    return som

def iscamacho(n):
    return camachosom(n) == n

def volgende_camacho(n):
    while not iscamacho(n):
        n += 1
    return n
