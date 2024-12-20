# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):# функция которая принимает три параметра со значениями по умолчанию.
    print(a, b, c)

# Вызовы функции с различным количеством аргументов
print_params()  # Без аргументов
print_params(10)  # Один аргумент
print_params(b=25)  # Изменение только b
print_params(c=[1, 2, 3])  # Изменение только c
print_params(5, 'текст', False)  # Все три аргумента

# 2. Распаковка параметров
values_list = [3.14, 'пример', False] # список
values_dict = {'a': 42, 'b': 'текст', 'c': True} # словарь

print_params(*values_list)  # Распаковка списка
print_params(**values_dict)  # Распаковка словаря

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)