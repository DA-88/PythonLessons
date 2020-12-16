import random

a = int(); k = int()
l = list()

a = 0
while a < 20:
    l.append(random.randint(0, 10))
    a += 1

k = int(input("Введите число: "))
print([el for el in l if el > k])
