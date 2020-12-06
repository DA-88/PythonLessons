s = input("Введите фразу: ")

pos = 1
for el in s.split(" "):
    if el != "":
        print(f"{pos}: {el[:10]}")
        pos += 1
