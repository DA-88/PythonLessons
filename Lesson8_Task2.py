class MyDivision(Exception):
    def __init__(self, *args, **kwargs):
        self.text=args[0]

def division(a,b):
    if not b:
        raise MyDivision("Делить на 0 нельзя!")
    else:
        return a/b


try:
    division(2,0)
except Exception as err:
    print(type(err), err)
