def fill_dict(str):
    global res_dict
    str = str.replace("\n", "")
    str = str.strip()
    while str.find("  ") != -1:
        str = str.replace("  ", " ")

    l = str.split(" ")
    res_dict[len(res_dict) + 1] = l


my_f = open("test3.txt", "r")
res_dict = {}
for line in my_f:
    fill_dict(line)
print(res_dict)
sum = 0
for el in res_dict:
    sum += float(res_dict[el][1])
    if float(res_dict[el][1]) < 20000:
        print(res_dict[el][0])
print(f"Средняя заработная плата - {round(sum / len(res_dict), 2)} рублей")
