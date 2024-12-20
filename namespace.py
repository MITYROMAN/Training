def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Вызовем inner_function внутри test_function


# Вызовем test_function
test_function()

# Попробуем вызвать inner_function вне test_function
try:
    inner_function()  # Это вызовет ошибку
except NameError as e:
    print(e)  # Выведем сообщение об ошибке