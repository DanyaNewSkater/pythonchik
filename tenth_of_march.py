students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася": 4, "Петя": 9, "Марина": 8, "Люба": 4, "Коля": 5, "Ваня": 10}
marks = {'Mary': [5, 8, 9, 10, 3, 5, 6, 6],
         'John': [3, 3, 6, 8, 2, 1, 8, 5],
         'Alex': [4, 4, 7, 4, 7, 3, 2, 9],
         'Patricia': [2, 1, 6, 8, 2, 3, 7, 4]}
categories = {'отлично': [8, 9, 10],
              'хорошо': [6, 7],
              'удовлетворительно': [4, 5],
              'неуд': [0, 1, 2, 3]}
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}


def ex_1(st, gr):
    mass = []
    for item in st:
        mass1 = []
        if item in gr.keys():
            mass1.append(item)
            mass1.append(gr[item])
            mass.append(mass1)
        else:
            mass1.append(item)
            mass1.append(" Контрольную работу не писал(а)")
            mass.append(mass1)
    return mass


def ex_1_1(st, gr):
    mass = []
    for item in gr.keys():
        if item in st and gr[item] >= 8:
            mass.append(item)
    return mass


def ex_1_2(st, gr):
    good = []
    bad = []
    g_and_b = []
    for item in gr.keys():
        if item in st and gr[item] >= 8:
            good.append(item)
        else:
            bad.append(item)
    g_and_b.append(good)
    g_and_b.append(bad)
    return g_and_b


def ex_2(mark, num):
    s = 0
    count = 0
    for i in mark.keys():
        s += mark[i][num-1]
        count += 1
    stroka = f"Курс {num} - {round(s/count)}"
    return stroka


def ex_4(mark, categ, num):
    qual = ""
    kurs = int(ex_2(mark, num)[-1])
    for item in categ.keys():
        if kurs in categ[item]:
            qual += ex_2(mark, num)[0:-1]
            qual += item
    return qual


def ex_5(mark, num):
    count = 0
    for item in mark.keys():
        for i in mark[item]:
            if i >= num:
                count += 1
    return count


def ex_7(q):
    two = list(map(len, [item.split() for item in q])).count(2)
    three = list(map(len, [item.split() for item in q])).count(3)
    result = f"Поисковых запросов, содержащих 2 слов(а): {round(two/(two+three)*100, 2)}%\n Поисковых запросов, содержащих 3 слов(а): {round(three/(two+three)*100,2)}%"
    return result


def ex_8(res):
    for item in res.keys():
        results[item]["ROI"] = round((results[item]["revenue"]/results[item]["cost"]-1)*100,2)
    return res


print(ex_1(students, grades))
print(ex_1_1(students, grades))
print(ex_1_2(students, grades))
print(ex_2(marks, 2))
print(ex_4(marks, categories, 2))
print(ex_5(marks, 5))
print(ex_7(queries))
print(ex_8(results))
