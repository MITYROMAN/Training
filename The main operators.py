def generate_password(n):
    password = ""  # Переменная для хранения пароля
    pairs_used = set()  # Множество для хранения уже использованных пар для проверки уникальности

    # Перебираем все возможные пары (i, j) где 1 <= i < j <= 20
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j  # Сумма пары
            if n % pair_sum == 0:  # Проверка, кратно ли n сумме пары
                # Формируем пару как строку 'ij'
                pair_str1 = f"{i}{j}"
                pair_str2 = f"{j}{i}"

                if pair_str1 not in pairs_used:  # Проверяем на уникальность
                    password += pair_str1
                    pairs_used.add(pair_str1)

                if pair_str2 not in pairs_used:  # Проверяем на уникальность
                    password += pair_str2
                    pairs_used.add(pair_str2)

    return password


# Запрашиваем у пользователя число от 3 до 20
n = int(input("Введите число от 3 до 20: "))
while n < 3 or n > 20:
    n = int(input("Некорректный ввод. Попробуйте снова (от 3 до 20): "))

result = generate_password(n)
print(f"Пароль для числа {n}: {result}")
