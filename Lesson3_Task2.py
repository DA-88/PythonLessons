def Concat(Name, Surname, BirthDate, City, Tel):
    return(f"{Name} {Surname} {BirthDate} {City} {Tel}")


print(Concat(input("Имя: "), input("Фамилия: "), input("Дата рождения: "), input("Город: "), input("Телефон: ")))
