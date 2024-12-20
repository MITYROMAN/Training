# Глобальная переменная для подсчета вызовов функций
calls = 0

def count_calls(): # Функция count_calls подсчитывающая вызовы остальных функций
    global calls
    calls += 1

def string_info(string): # Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
    count_calls() # Функция count_calls подсчитывающая вызовы остальных функций
    # Возвращаем кортеж с длиной строки и строками в верхнем и нижнем регистре
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search): # Функция is_contains принимает два аргумента:строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует
    count_calls()  # Функция count_calls подсчитывающая вызовы остальных функций
    # Приводим искомую строку к нижнему регистру для сравнения
    string_lower = string.lower()
    # Проверяем, есть ли строка в списке (все элементы списка также приводим к нижнему регистру)
    return string_lower in (s.lower() for s in list_to_search)

# Примеры вызовов функций
print(string_info('Capybara'))  # Ожидается: (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # Ожидается: (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Ожидается: True
print(is_contains('cycle', ['recycling', 'cyclic']))  # Ожидается: False

# Выводим общее количество вызовов функций
print(calls)  # Ожидается: 4