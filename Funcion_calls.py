def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []

    # Проверяем, что n и m больше нуля
    if n <= 0 or m <= 0:
        return matrix  # Возвращаем пустой список

    # Внешний цикл для создания n строк
    for i in range(n):
        row = []  # Создаем пустой список для строки
        # Внутренний цикл для заполнения строки m значениями
        for j in range(m):
            row.append(value)  # Заполняем строку значением value
        matrix.append(row)  # Добавляем заполненную строку в матрицу

    return matrix  # Возвращаем заполненную матрицу


result1 = get_matrix(2,2,10)
result2=get_matrix(3,5,42)
result3 = get_matrix(4,2,13)

print(result1)  # Выведет: [[10, 10], [10, 10]]
print(result2)  # Выведет: [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
print(result3)  # Выведет: [[13, 13], [13, 13], [13, 13], [13, 13]]

# Тест на случай, если n или m <= 0
result_invalid = get_matrix(0, 3, 5)
print(result_invalid)  # Выведет: []