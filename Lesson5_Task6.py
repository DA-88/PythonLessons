import re

f_obj = open("test6.txt", "r")
res_dict = {}

for line in f_obj:
    key = ""
    l = re.findall("^.*?:", line)
    if len(l) > 0:
        key = l[0][:len(l[0]) - 1]
    sum=0
    l=[]
    l=re.findall("\d+", line)
    if len(l) > 0:
        for el in l:
            sum+=int(el)
    if key != "":
        res_dict[key]=sum

f_obj.close()
print(res_dict)
