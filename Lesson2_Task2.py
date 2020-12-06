a = list(input('Введите элементы: '))

i = 0
while i < len(a)-1:
    a[i], a[i+1] = a[i+1], a[i]
    i += 2

print(a)
