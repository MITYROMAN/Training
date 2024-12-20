    # true_math.py


from math import inf


def divide(first, second):
    """Функция для деления, возвращает бесконечность при делении на 0."""
    if second == 0:
        return inf
    return first / second