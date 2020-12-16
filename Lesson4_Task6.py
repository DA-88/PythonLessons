from itertools import count
from itertools import cycle

start_el = int(input("Введите начальное значение: "))
end_el = int(input("Введите конечное значение: "))
l_str = input("Введите строку: ")

for el in count(start_el):
    if el > end_el:
        break
    else:
        print(el)

с = 0
for el in cycle(l_str):
    if с > end_el:
        break
    print(el)
    с += 1
