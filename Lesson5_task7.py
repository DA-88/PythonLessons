import json


def list_from_str(str):
    global res_dict
    str = str.replace("\n", "")
    str = str.strip()
    while str.find("  ") != -1:
        str = str.replace("  ", " ")

    return (str.split(" "))


my_f = open("test7.txt", "r")
profit = {}
average_profit = {}
sum = 0
for line in my_f:
    l = list_from_str(line)
    profit[l[0]] = int(l[2]) - int(l[3])
    sum += profit[l[0]]
my_f.close()

average_profit["average_profit"] = sum / len(profit)
my_f = open("test7_out.json", "w")
json.dump([profit, average_profit], my_f)
my_f.close()
