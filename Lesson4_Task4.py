import random

a = int()
l = list()

a = 0
while a < 20:
    l.append(random.randint(0, 10))
    a += 1
print(l)
print([el for el in l if l.count(el) == 1])
