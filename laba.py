documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

a = "a"
x = 0

while (a != "q"):
    x += 1
    a = input(f"{x}.\nВведите команду: ")

    if a == "p":
        o = 0
        b = input("Введите номер документа: ")
        print("Результат: ")
        for item in documents:
            if item["number"] == b:
                print("Владелец документа: " + item["name"])
                o += 1
        if o == 0:
            print("Документ не найден в базе")

    if a == "s":
        o = 0
        b = input("Введите номер документа: ")
        print("Результат: ")
        for i in directories:
            for j in directories[i]:
                if j == b:
                    print("Документ хранится на полке: " + str(i))
                    o += 1
        if o == 0:
            print("Документ не найден в базе")


    def polka(num):
        for it in directories.keys():
            if num in directories[it]:
                return it

    def i(documents):
        stroka = ''
        for item in documents:
            stroka += f"№: {str(item['number'])}, тип: {str(item['type'])}, владелец: {str(item['name'])}, полка хранения: {polka(item['number'])}\n"
        return stroka

    if a == "i":
        print("Результат: ")
        print(i(documents))

    if a == "ads":
        b = input("Введите номер полки: ")
        o = 0
        print("Результат: ")
        for i in directories:
            if i == b:
                o += 1
                break
        if o == 0:
            directories[b] = []
            print(f"Полка добавлена. Текущий перечень полок: {list(map(int,[i for i in directories.keys()]))}")
        else:
            print(f"Такая полка уже существует. Текущий перечень полок: {list(map(int,[i for i in directories.keys()]))}")

    if a == "ds":
        b = input("Введите номер полки: ")
        o = 0
        b1 = ""
        for i in directories.keys():
            if i == b:
                o += 1
                b1 = i
                break
        if o != 0:
            if directories[b1] == []:
                del directories[b1]
                print(f"Полка удалена. Текущий перечень полок: {list(map(int,[i for i in directories.keys()]))}")
            else:
                print(f"На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: {list(map(int,[i for i in directories.keys()]))}")
        else:
            print(f"Такой полки не существует. Текущий перечень полок: {list(map(int,[i for i in directories.keys()]))}")

    if a == "ad":
        b = input("Введите номер документа: ")
        documents.append("[]")
        documents[-1] = dict({'number': b})
        b = input("Введите тип документа: ")
        documents[-1]["type"] = b
        b = input("Введите владельца документа: ")
        documents[-1]["name"] = b
        b = input("Введите полку для хранения: ")
        print("Результат: ")
        if b in directories.keys():
            for item in directories.keys():
                if item == b:
                    directories[item].append(documents[-1]["number"])
                    break
            print(f"Документ добавлен. Текущий список документов: \n {i(documents)}")
        else:
            print(f"Такой полки не существует. Добавьте полку командой ads. \n \n Текущий список документов: {i(documents)}")

    if a == "d":
        b = input("Введите номер документа: ")
        b1 = ''
        o = 0
        print("Результат\n")
        for item in documents:
            if item["number"] == b:
                b1 = item
                o += 1
                break
        if o != 0:
            documents.remove(b1)
            directories[polka(b)].remove(b)
            print(f"Документ удален.\nТекущий список документов:\n{i(documents)}")
        else:
            print(f"Документ не найден в базе.\nТекущий список документов:\n{i(documents)}")
            
    if a == "m":
        b = input("Введите номер документа: ")
        b1 = input("Введите номер полки:")
        o = 0
        print("Результат: \n")
        for it in documents:
            if it["number"] == b:
                o += 1
                break
        if b1 in directories.keys() and o != 0:
            directories[polka(b)].remove(b)
            directories[b1].append(b)
            print(f"Документ перемещен.\nТекущий список документов:\n{i(documents)}")
        elif o != 0:
            print(f"Такой полки не существует. Текущий перечень полок: {list(map(int,[i for i in directories.keys()]))}")
        else:
            print(f"Документ не найден в базе.\n Текущий список документов: \n {i(documents)}")
