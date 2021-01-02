my_f = open("test4.txt", "r")
f_obj = open("test4_out.txt", "w")

for line in my_f:
    line = line.replace("One", "Один")
    line = line.replace("Two", "Два")
    line = line.replace("Three", "Три")
    line = line.replace("Four", "Четыре")
    f_obj.write(line)
my_f.close()
f_obj.close()
