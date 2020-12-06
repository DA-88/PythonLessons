StopFlag = False
MainList = []
Pos = 1

while not StopFlag:
    d = {}
    d["Название"] = input("Введите назвавние ")
    d["Цена"] = input("Введите цену ")
    d["Количество"] = input("Введите количество ")
    d["Ед"] = input("Введите единицу измерения ")
    StopFlag = True if input("Стоп (+ / -)? ") == "+" else False
    MainList.append((Pos, d))
    Pos += 1

d_out = {}
for el in MainList:
    el = el
    for dl in el[1]:
        if d_out.get(dl) is None:
            d_out[dl] = list(el[1][dl])
        else:
            d_out[dl].append(el[1][dl])

print(d_out)