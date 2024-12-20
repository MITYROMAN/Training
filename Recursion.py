def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку

    if len(str_number) == 1:  # Базовый случай
        return int(str_number) if str_number != '0' else 1  # Если '0', то возвращаем 1;# Если '0', то возвращаем 1

    first = int(str_number[0])  # Извлекаем первую цифру
    if first == 0:  # Если первая цифра 0, пропускаем её; # Если первая цифра 0, пропускаем её
        return get_multiplied_digits(int(str_number[1:]))  # Рекурсивный вызов на оставшихся
    return first * get_multiplied_digits(int(str_number[1:]))  # Умножаем на результат рекурсии

result1 = get_multiplied_digits(40203)
print(result1)  # Ожидаемый вывод: 24

result2 = get_multiplied_digits(402030)
print(result2)  # Ожидаемый вывод: 24
