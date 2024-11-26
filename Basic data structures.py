grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={"Johnny","Bilbo","Steve","Khendrik","Aaron"}
# Сортировка имен студентов
sorted_students = sorted(students)# в алфавитном порядке
# Функция для вычисления средних баллов
def create_average_grades_dict(grades, sorted_students):# сопоставить имя и оценку
    average_grades = {} # имена студентов и баллов
    # Сопоставление студентов с оценками
    for student, grade_list in zip(sorted_students, grades): # zip позволяет нам получить  студент + оценка,for и in  действия с элементоми.
        # Вычисляем средний балл
        average_grades[student] = sum(grade_list) / len(grade_list)
    return average_grades # завершает выполнение и возврашается к студентам и баллам
# Генерация словаря со средними баллами
average_grades_dict = create_average_grades_dict(grades, sorted_students)
# Результат
print(average_grades_dict)
