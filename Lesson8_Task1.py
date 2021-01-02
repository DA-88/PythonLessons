from datetime import datetime

class Date:
    date = "01-01-1998"

    def __init__(self, date):
        self.date = date
        Date.date = date

    @staticmethod
    def check_date(date: str):
        res = True
        x = date.split("-")
        if not (int(x[0]) >= 1 and int(x[0]) <= 31): res = False
        if not (int(x[1]) >= 1 and int(x[1]) <= 12): res = False
        if not (int(x[2]) >= 1 and int(x[2]) <= 3000): res = False
        return res
    @classmethod
    def strptime(cls):
        return datetime.strptime(cls.date, '%d-%m-%Y')


m = Date("07-07-2007")
print(Date.check_date("17-01-2021"))
print(Date.strptime())