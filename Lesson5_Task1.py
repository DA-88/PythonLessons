f_obj = open("test.txt", "w")
s = input("Введите строку: ")

while s != '':
    f_obj.write(f"{s}\n")
    s = input("Введите строку: ")
f_obj.close()
