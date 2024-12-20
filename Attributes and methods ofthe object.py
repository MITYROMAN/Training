class House:
    def __init__(self, name, number_of_floors):
        self.name = name                  # Имя дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)            # Выводим этажи от 1 до new_floor
        else:
            print("Такого этажа не существует")  # Этаж вне диапазона

# Создаем объекты класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to
h1.go_to(5)    # Ожидается вывод: 1, 2, 3, 4, 5
h2.go_to(10)   # Ожидается вывод: "Такого этажа не существует"