import math, random, statistics


def my_log(lst: list) -> list:
    return list(map(lambda x: math.log(x) if (x > 0) else None, lst))


spis = [1, 3, 2.5, -1, 9, 0, 2.71]
print(my_log(spis))

mass = []
mass1 = []
for i in range(random.randint(10, 20)):
    mass.append(random.randint(50, 100))
print(mass)
maxim = mass.index(max(mass))
misha = mass.index(min(mass))
if misha < maxim:
    print(statistics.mean(mass[misha:maxim]))
else:
    mass1 += mass[0:maxim+1]
    mass1.append(statistics.median(mass[maxim+1: misha]))
    mass1 += mass[misha:-1]
    mass1.append(mass[-1])
    print(mass1)

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

text = """Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick"""
print([i.split() for i in text.split("\n")])
