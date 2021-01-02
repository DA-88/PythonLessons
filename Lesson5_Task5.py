import random


def CreateString():
    WordsLimit = random.randint(10, 100)
    a = 1
    res = ""
    while a <= WordsLimit:
        res = f"{res} {random.randint(0, 1000)}"
        a += 1
    res = res.strip()
    res = f"{res}\n"
    return res


def calc_string_sum(str):
    res = 0
    str = str.replace("\n", "")
    str = str.strip()
    while str.find("  ") != -1:
        str = str.replace("  ", " ")

    l = str.split(" ")
    for el in l:
        res += int(el)
    return (res)


LinesLimit = random.randint(10, 100)
a = 1
f_obj = open("test5.txt", "w")
while a <= LinesLimit:
    f_obj.write(CreateString())
    a += 1
f_obj.close()

f_obj = open("test5.txt", "r")
res = 0
for line in f_obj:
    res += calc_string_sum(line)

print("Сумма чисел в файле: ", res)
