from functools import reduce


def func(a, b):
    return a * b


l = list(range(100, 1001, 2))

sum = 1
for el in l:
    sum *= el

print("Список: ", l)
print("Ответ:    ", reduce(func, l))
print("Контроль: ", sum)
