def calc(st: str)->int:
    lst = list()
    for item in list(st):
        if item.isdigit():
            lst.append(item)
        else:
            if item == "*":
                lst[-2] = int(lst[-1])*int(lst[-2])
                lst.remove(lst[-1])
            if item == "+":
                lst[-2] = int(lst[-1])+int(lst[-2])
                lst.remove(lst[-1])
            if item == "-":
                lst[-2] = int(lst[-2])-int(lst[-1])
                lst.remove(lst[-1])
    return lst[-1]

print(calc("123*+2+2-"))


def del_test(st: str) -> bool:
    lst = list()
    for item in list(st):
        lst.append(item)
        if len(lst)>=2:
            if (lst[-1] == ")" and lst[-2] == "(") or (lst[-1] == "]" and lst[-2] == "[") or (
                    lst[-1] == "}" and lst[-2] == "{"):
                lst.pop(-1)
                lst.pop(-1)
    if lst:
        return False
    return True
  
print(del_test("[({})][]"))


stroka = """Край любимый! Сердцу снятся
Скирды солнца в водах лонных,
Я хотел бы затеряться
В зеленях твоих стозвонных.
"""
file = open("text.txt", "w")
file.write(stroka)
file.close()
def update(fn:str, ln:str):
    try:
        file1 = open(fn)
    except FileNotFoundError:
        return "no such file"
    file2 = file1.read().split("\n")[:-1]
    file1.close()
    for i in range(len(file2)):
        file2[i] = f"{i + 1}. " + file2[i]
    n = "\n".join(file2)
    file3 = open(ln, "w")
    file3.write(n)
    file3.close()
    file4 = open(ln)
    fr = file4.read()
    file4.close()
    return fr

print(update("text.txt", "update_text.txt"))


import requests

file = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat").text
file1 = file.split("\n")[:-1]
sp = list()
for i in range(len(file1)):
    file1[i] = file1[i].split(",")
    if file1[i][0]=="Количество заявок на потребительские кредиты":
        file1[i][-1] = int(file1[i][-1])
        sp.append(file1[i])
res = dict()
res_n = 0
for it in range(len(sp)):
    if it < len(sp)-1:
        if sp[it][1] == sp[it + 1][1]:
            res_n += sp[it][-1]
            res_n += sp[it + 1][-1]
        else:
            res[sp[it - 1][1]] = res_n
            res_n = 0
res.pop("Россия")

mv = max(res.values())
for itt in res.keys():
    if res[itt] == mv:
        print(itt)
        break
