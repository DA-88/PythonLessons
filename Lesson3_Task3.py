def Sum3(a1, a2, a3):
    if a1 > a2:
        return a1 + max(a2, a3)
    else:
        return a2 + max(a1, a3)


a1 = float(input("A1: "))
a2 = float(input("A2: "))
a3 = float(input("A3: "))

print(Sum3(a1, a2, a3))
