n = int(input())
e = int(input())
w = int(input())
end = input()

acum = 0
won = 0

for i in range(1,n+1):
    acum += e
    won += acum

    doubled = False
    if i % w == 0:
        if i != n or end == 'gestopt':
            doubled = True
            won *= 2

    if i == n and end == 'verloren':
        won -= acum
        won /= 2

    print(f'tafel #{i}{' (x2)' if doubled else '' }: €{int(won)}')