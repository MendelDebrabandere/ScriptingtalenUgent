a = int(input())
b = int(input())
c = int(input())

z = (a+b-b*c)/(c-1)
m = z + a

print(f"The mother is {int(round(m*12,0))} months old and her son {int(round(z*12,0))} months.")
