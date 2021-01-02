def Division2(a, b):
    try:
        a = float(a); b = float(b)
    except:
        return "Аргументы должны быть числами!"

    if b!=0:
        return a/b
    else:
        return "Деление на 0!"


a = input("Введите 1 число: ")
b = input("Введите 2 число: ")
print(Division2(a, b))
