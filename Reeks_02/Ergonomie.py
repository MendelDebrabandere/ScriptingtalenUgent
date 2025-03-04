def positie(ch):
    idx = ord(ch.lower()) - ord('a')

    rij = idx // 13
    kolom = idx % 13

    return rij, kolom


def verschuiving(ch1, ch2):
    rij1, kolom1 = positie(ch1)
    rij2, kolom2 = positie(ch2)

    return abs(rij1 - rij2) + abs(kolom1 - kolom2)


def ergonomie(word):
    som = 0
    for idx in range(len(word)-1):
        som += verschuiving(word[idx], word[idx+1])
    return som
