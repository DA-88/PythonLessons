def GetSum(str):
    global ResultSum
    ResultSum = ResultSum + float(str)


ResultSum = 0
StopFlag = False

while not StopFlag:
    s = input("Введите строку: ")
    k = s.split(" ")
    for v in k:
        if v == "*": StopFlag = True
        if not StopFlag: GetSum(v)

    print("Результат: ", ResultSum)
