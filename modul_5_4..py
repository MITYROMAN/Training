class House:
    houses_history = []  # Атрибут класса для хранения истории домов

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю при создании объекта
        house_name = args[0]  # Название объекта передается первым аргументом
        cls.houses_history.append(house_name)
        print(f"Создан дом: {house_name}.")
        return super().__new__(cls)

    def __del__(self):
        # Выводим сообщение о сносе дома
        print(f"{self.first} снесён, но он останется в истории")

    def __init__(self, name, floors):
        self.first = name  # Название дома
        self.floors = floors  # Количество этажей

# Пример создания объектов класса House

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
del h1