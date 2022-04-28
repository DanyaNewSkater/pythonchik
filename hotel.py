class Hotel:
    def __init__(self, num_rooms):
        self._rooms = dict()
        self._rooms["SGL"] = [0 for _ in range(num_rooms)]
        self._rooms["DBL"] = [0 for _ in range(num_rooms)]
        self._rooms["Junior"] = [0 for _ in range(num_rooms)]
        self._rooms["Junior Suite"] = [0 for _ in range(num_rooms)]
        self._rooms["Suite"] = [0 for _ in range(num_rooms)]

        self._prices = dict()
        self._prices["SGL"] = 1000
        self._prices["DBL"] = 1750
        self._prices["Junior"] = 750
        self._prices["Junior Suite"] = 1250
        self._prices["Suite"] = 2250

    # метод для бронирования номера по уникальному значению в списке
    def occupy(self, room_id, room_type):
        if self._rooms[room_type][room_id] == 0:
            self._rooms[room_type][room_id] = 1  # бронируем номер
        else:
            raise RuntimeError("Номер занят")

    # метод для освобождения номера по уникальному значению в списке
    def free(self, room_id, room_type):
        self._rooms[room_type][room_id] = 0  # освобождаем номер

    def __str__(self):
        a = ''
        for i in self._rooms:
            for j in range(len(self._rooms[i])):
                if self._rooms[i][j] == 0:
                    a += 'Класс ' + i + ' Номер ' + str(j + 1) + " свободен\n"
                else:
                    a += 'Класс ' + i + ' Номер ' + str(j + 1) + " занят\n"
        return a

    def all_occupy(self):
        for i in self._rooms:
            for j in range(len(self._rooms[i])):
                self._rooms[i][j] = 1

    def occ_to_all(self):
        o = 0
        for i in self._rooms:
            for j in self._rooms[i]:
                if j == 1:
                    o += 1
        return round(o/len(self._rooms)*4, 2)

    def all_free(self):
        for i in self._rooms:
            for j in range(len(self._rooms[i])):
                self._rooms[i][j] = 0

    def income(self):
        count = 0
        for i in self._rooms:
            for j in self._rooms[i]:
                if j == 1:
                    count += self._prices[i]
        return count




hotel = Hotel(5)  # в нашем отеле, например, 5 номеров
print(hotel._rooms)  # смотрим номера через атрибут self.rooms
hotel.occupy(3, "DBL")
print(hotel._rooms)
hotel.free(3, "DBL")
hotel.all_occupy()
print(hotel.income())
print(hotel.__str__())
