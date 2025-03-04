k = float(input())
l = float(input())

if l > 10000:
    print("superreuzen (a)")
elif l > 1000:
    print("superreuzen (b)")
elif l > 100 and k < 7500:
    print("heldere reuzen")
elif l > 10 and k < 6000:
    print("reuzen")
elif (l < 0.01 and k > 5000) or (l < 0.0001 and k > 3000):
    print("witte dwergen")
else:
    print("hoofdreeks")