income = float(input("Введите выручку: "))
outcome = float(input("Введите издержки: "))

if income > outcome:
    print("Поздравляем, Вы отработали с прибылью! Рентабелность составила:", income / outcome)
    pers = int(input("Введите численность персонала: "))
    print("Прибыль на одного сотрудника составила: ", (income - outcome) / pers)
elif income < outcome:
    print("Вы получили убыток...")
else:
    print("Вы сработали в ноль...")