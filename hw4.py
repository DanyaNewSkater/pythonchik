import math
import random


def my_log(lst: list) -> list:
    return list(map(lambda x: math.log(x) if (x > 0) else None, lst))


spis = [1, 3, 2.5, -1, 9, 0, 2.71]
print(my_log(spis))

mass = []
meann = 0
mass1 = []
med = 0
mass2 = []
for i in range(random.randint(5, 20)):
    mass.append(random.randint(1, 1000))
print(mass)
if mass.index(max(mass)) - mass.index(min(mass)) <= -1:
    mass1 = mass[mass.index(max(mass))+1:mass.index(min(mass))]
    meann = sum(mass1)/len(mass1)
    print(meann)
elif mass.index(max(mass)) - mass.index(min(mass)) >= 1:
    mass1 = mass[mass.index(min(mass)) + 1:mass.index(max(mass))]
    mass1 = sorted(mass1)
    if len(mass1) % 2 == 0:
        med = sum(mass1[math.floor(len(mass1) / 2):math.floor(len(mass1) / 2) + 2]) / 2
    else:
        med = mass1[math.floor(len(mass1)/2)]
    mass2 = mass[0:mass.index(min(mass))+1]
    mass2.append(med)
    mass2 += mass[mass.index(max(mass)):-1]
    mass2.append(mass[-1])
    print(mass2)


n = [1, 5, 6.3, 6, None, 2.0, -4, None]
meannn = 0
count = 0
for t in n:
    if t != None:
        meannn += t
        count += 1
for tt in n:
    if tt == None:
        n[n.index(tt)] = meannn/count
print(n)

text = """Call me Ishmael. Some years ago - never mind how long precisely - having\n
little or no money in my purse, and nothing particular to interest me\n
on shore, I thought I would sail about a little and see the watery part\n
of the world. It is a way I have of driving off the spleen, and regulating\n
the circulation. - Moby Dick\n"""
sp = []
spfor = []
text = text.split()
for item in text:
    if item.endswith("\n") and len(item)-2 > 3:
        sp.append(spfor)
        spfor = []
    if len(item) > 3:
        spfor.append(item)
        print(spfor)
print(sp)

