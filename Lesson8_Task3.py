
class ListTypeException(Exception):
    def __init__(self, *args, **kwargs):
        self.text=args[0]

def append_result(el):
    global result
    if type(el) is int:
        result.append(el)
    else:
        raise ListTypeException("Это не число!")

result=[]
a=input("Введите значение: ")
while a !="stop":
    a = input("Введите значение: ")
    try:
        append_result(int(a))
    except Exception as err:
        print(type(err), err)


print(result)
