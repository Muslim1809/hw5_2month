# Функция пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # обмен
    return arr

# Функция двоичного поиска
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"Элемент {target} найден на индексе {mid}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Элемент {target} не найден")
    return -1

# Пример списка для сортировки и поиска
arr = [64, 34, 25, 12, 22, 11, 90]

# Сортировка списка
sorted_arr = bubble_sort(arr)
print("Отсортированный список:", sorted_arr)

# Поиск элемента
target = 22
binary_search(sorted_arr, target)
