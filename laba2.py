import json

f = [{"category": "cat1", "name": "task1", "time": "222"}, {"category": "cat2", "name": "task2", "time": "444"}]
data = json.dumps(f)
with open("file.json","w") as file:
    json.dump(data, file)
with open("file.json") as file1:
    file3 = json.load(file1)
file4 = json.loads(file3)
a = input("1  - добавление задачи \n2 - показ задач\n3 - выход\nВведите число: ")
while a != "3":
    if a == "1":
        d = dict()
        file4.append(d)
        st = input("Сформулируйте задачу: ")
        d["name"] = st
        st = input("Добавьте категорию к задаче: ")
        d["category"] = st
        st = input("Добавьте время к задаче: ")
        d["time"] = st
        a = input("1  - добавление задачи \n2 - показ задач\n3 - выход\nВведите число: ")
    if a == "2":
        for item in file4:
            print(f"Задача: {item['name']}  Категория: {item['category']}  Дата: {item['time']}")
        a = input("1  - добавление задачи \n2 - показ задач\n3 - выход\nВведите число: ")
