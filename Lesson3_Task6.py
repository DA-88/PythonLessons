def int_func(str):
    return str.capitalize()


str = input("Введите строку: ")

l = str.split(" ")
r = list()

for v in l:
    r.append(int_func(v))
print(" ".join(r))
