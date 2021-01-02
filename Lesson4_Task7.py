def simple_factorial(target_value):
    curent_pos = 1
    res = 1
    while curent_pos <= target_value:
        res *= curent_pos
        yield res
        curent_pos += 1


n = int(input("Введите значение: "))
c = simple_factorial(n)

print(c)

for el in c:
    print(el)