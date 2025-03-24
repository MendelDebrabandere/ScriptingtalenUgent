def checkwoord(w, lijn):
    return w == lijn


woord = input()
w = woord.lower()
n = int(input())

for rij in range(n):
    row = input().lower()

    for idx, c in enumerate(row):
        found = False
        if c == w[0]:
            found = checkwoord(w, row[idx:idx+len(w)])
        if c == w[-1]:
            found = checkwoord(w, row[idx:idx+len(w)][::-1])

        if found:
            print(f'{woord} staat op rij {rij} en kolom {idx}')
            exit(0)



print(f'{woord} werd niet gevonden')