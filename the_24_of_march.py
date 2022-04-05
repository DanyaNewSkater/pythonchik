import requests,statistics,matplotlib.pyplot as plt

try:
    fir = int(input("Ввод: "))
    sec = int(input())
    oper = input()
    res = 0
    if oper == "/":
        res = fir/sec
    if oper == "*":
        res = fir*sec
    if oper == "+":
        res = fir+sec
    if oper == "-":
        res = fir-sec
except ZeroDivisionError:
    print("Вывод: ошибка деления на ноль")
except ValueError:
    print("Вывод: ошибка преобразования типов")
else:
    print(f"Вывод: {res}")
    
    
s = str(requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat").content).split("\\n")
s[0] = "8.9"
s = list(map(float,s[0:-1]))
print("max = ",max(s),"\nmin = ", min(s),"\nmean = ",  statistics.mean(s),"\nunique =  ", len(set(s)))
plt.plot(list(range(0,len(s))),s)
plt.show()


stt = str(requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt").content).lower()
trantab = str.maketrans({'"': " ", '-': " ", '.': " ", ';': " ",':': " ", ',': " "})
stt = stt[0:-2]
stt = stt.translate(trantab).split("\\n")
stt[0] = stt[0][1:]
stt[-1] = stt[-1][:-1]
stt = " ".join(stt)
while "  " in stt:
    stt = stt.replace("  "," ")
print(stt)
print("\n".join(stt.split()))
file = open("moby_clean.txt","w")
file.write("\n".join(stt.split()))
file.close()


file = open("moby_clean.txt").read()
d = dict()
sort_dict1 = dict()
for i in file.split("\n"):
    d[i] = 0
for it in file.split(("\n")):
    d[it] +=1
sorted_val1 = sorted(d.values(),reverse=True)
for item in sorted_val1:
    for items in d.keys():
        if d[items] == item:
            sort_dict1[items] = item
print([i for i in sort_dict1.keys()][:5]," ",[i for i in sort_dict1.keys()][-5::])

def same(a: str, b: str):
    a1 = open(a).read().split()
    b1 = open(b).read().split()
    res1 = []
    res2 = []
    res1 = a1 + b1
    for i in a1:
        if i in b1:
            res2.append(i)
    return res1+res2

  
a = input("Задайте мне вопрос!!! (если хотите закончить, напечатайте end) ")
while a != "end":
    s = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt").text.split("\n")
    print(s[random.randint(0, len(s) - 1)])
    a = input("Задайте мне вопрос!!! (если хотите закончить, напечатайте end) ")


s = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt").text.lower()
d = dict()
trantab = s.maketrans({'"': " ", '-': " ", '.': " ", ';': " ",':': " ", ',': " "})
s = s.translate(trantab)
print(s)
s = s.split()
for i in s:
    d[i]=0
for i in s:
    d[i]+=1
print(d)


s = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt").text.split()
probel = len(s)-1
up = 0
dig = 0
chars = [item for sublist in list(map(list,s)) for item in sublist]
for it in chars:
    if it.isdigit():
        dig+=1
    if it.upper() == it:
        up+=1
print(f"Верхний регистр: {up} \n Чисел: {dig} \n Пробелов: {probel}")
