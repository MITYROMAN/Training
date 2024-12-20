# module_4_1.py

from fake_math import divide as fake
from true_math import divide as true

# Тестируем функции с различными значениями
result1 = fake(69, 3)  # Ожидаем 23.0
result2 = fake(3, 0)    # Ожидаем 'Ошибка'
result3 = true(49, 7)   # Ожидаем 7.0
result4 = true(15, 0)    # Ожидаем inf

# Вывод результатов
print(result1)
print(result2)
print(result3)
print(result4)





