def count_words_in_string(str):
    str = str.replace("\n", "")
    str = str.strip()
    while str.find("  ") != -1:
        str = str.replace("  ", " ")

    l = str.split(" ")
    if l[0] == "":
        return (0)
    else:
        return (len(l))


my_f = open("test.txt", "r")
string_count = 0
for line in my_f:
    string_count += 1
    print(f"Строка номер {string_count}: количество слов - {count_words_in_string(line)}")
print(f"Всего строк - {string_count}")
