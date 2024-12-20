nums = [5,6,2,1,3,4]

def bubble_sort(ls):
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(ls)-1):
            if ls[i]>ls[i+1]:
                ls[i],ls[i+1]=ls[i+1],ls[i]
                swapped=True

# print(nums)
# print(bubble_sort(nums))

def selection_sort(ls):
    for i in range(len(ls)):
        lowest=i
        for j in range(i+1,len(ls)):
            if ls[j]<ls[lowest]:
                lowest=j
                ls[i],ls[lowest]=ls[lowest],ls[i]

selection_sort(nums)
print(nums)

nums = [5, 6, 2, 1, 3, 4]

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True

# Создадим копию nums для сортировки пузырьком
bubble_sorted_nums = nums.copy()
bubble_sort(bubble_sorted_nums)
print("Пузырьковая сортировка:", bubble_sorted_nums)


def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        # Меняем местами только после завершения внутреннего цикла
        ls[i], ls[lowest] = ls[lowest], ls[i]

# Создадим копию nums для сортировки выбором
selection_sorted_nums = nums.copy()
selection_sort(selection_sorted_nums)
print("Сортировка выбором:", selection_sorted_nums)






