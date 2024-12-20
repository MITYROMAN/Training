def calculate_structure_sum(*args):
    total_sum = 0

    for element in args:
        if isinstance(element, (int, float)):  # Проверяем на числа
            total_sum += element
        elif isinstance(element, str):  # Проверяем на строки
            total_sum += len(element)
        elif isinstance(element, list):  # Обработка списков
            total_sum += calculate_structure_sum(*element)
        elif isinstance(element, tuple):  # Обработка кортежей
            total_sum += calculate_structure_sum(*element)
        elif isinstance(element, set):  # Обработка множеств
            total_sum += calculate_structure_sum(*element)
        elif isinstance(element, dict):  # Обработка словарей
            # Суммируем ключи и значения словаря
            total_sum += calculate_structure_sum(*element.keys())  # Длина ключей
            total_sum += calculate_structure_sum(*element.values())  # Значения

    return total_sum

# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидается 99


