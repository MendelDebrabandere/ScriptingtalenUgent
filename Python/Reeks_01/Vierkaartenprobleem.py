eval = input()
val = input()
turned = input()

correct = True

if eval == "waarde":
    isEven = int(val) % 2 == 0
    correct = isEven if turned == 'ja' else not isEven
elif eval == "kleur":
    isRood = val == 'rood'
    correct = isRood if turned == 'nee' else not isRood

print(f'{'Juist' if correct else 'Fout'}: kaarten met {eval} {val} moeten {'' if (turned == 'ja') == correct else 'niet '}gedraaid worden.')

