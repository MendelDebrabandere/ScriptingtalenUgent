
x1 = input()

while x1 != 'stop':
    checksum = int(x1)
    for i in range(2,10):
        x = int(input())
        checksum += i * x

    x10 = int(input())

    if x10 == checksum % 11:
        print("OK")
    else:
        print("FOUT")

    x1 = input()

