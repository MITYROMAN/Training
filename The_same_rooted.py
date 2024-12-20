def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для хранения подходящих слов
    root_word_lower = root_word.lower()  # Приводим корневое слово к нижнему регистру для сравнения

    # Перебираем слова из других параметров
    for word in other_words:
        word_lower = word.lower()  # Приводим текущее слово к нижнему регистру,независимо от того, в каком регистре оно написано.
        # Проверяем, содержится ли либо root_word в word, либо наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем слово в список, если условие выполнено

    return same_words  # Возвращаем список

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты на экран
print(result1)  # Ожидаемый вывод: ['richiest', 'orichalcum', 'richies']
print(result2)  # Ожидаемый вывод: ['Able', 'Disable']