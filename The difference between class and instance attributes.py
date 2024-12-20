class Example:
    # Атрибут класса
    class_attribute = 'Это атрибут класса'

    def __new__(cls, *args, **kwargs):
        print("Вызов метода __new__")
        print("args:", args)
        print("kwargs:", kwargs)

        # Создаем новый объект
        instance = super().__new__(cls)

        # Можно добавить дополнительные действия перед инициализацией
        return instance

    def __init__(self, first, second, third):
        print("Вызов метода __init__")
        print("first:", first)
        print("second:", second)
        print("third:", third)

        # Атрибуты объекта
        self.first = first
        self.second = second
        self.third = third

    # Создание экземпляра класса


ex = Example('data', second=25, third=3.14)

# Доступ к атрибутам
print("Атрибут класса:", Example.class_attribute)
print("Атрибут объекта:", ex.first, ex.second, ex.third)