def MyFunc(x, y):
    return (x ** y)


def MyFunc2(x, y):
    res = x
    i = 1
    while i < abs(y):
        res = res * x
        i += 1

    if y > 0:
        return (res)
    elif y < 0:
        return (1 / res)
    else:
        return 0


x = int(input("X: "))
y = int(input("Y: "))

print(MyFunc(x, y))
print(MyFunc2(x, y))
