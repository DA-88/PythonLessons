start_v = float(input("Введите начальное значение: "))
target_v = float(input("Введите целевое значение: "))
day_num = int(1)

print("")
while start_v < target_v:
    print("В ", day_num, "-й день: ", start_v, "километров")
    day_num += 1
    start_v *= 1.1

print("Результат будет достигнут на ", day_num, " день")