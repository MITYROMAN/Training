# fake_math.py

def divide(first, second):
    """Функция для деления, возвращает 'Ошибка' при делении на 0."""
    if second == 0:
        return 'Ошибка'
    return first / second