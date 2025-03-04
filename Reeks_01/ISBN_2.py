som = 0
for i in range(1,10):
    getal = input()
    som += i * int(getal)

checksum = input()

if som % 11 == int(checksum):
    print("OK")
else:
    print("FOUT")