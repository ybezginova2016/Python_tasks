# СОРТИРОВКА ПОИСКОМ

# Написанный ниже код выполняет сортировку массива по возрастанию.
# Напишем функцию для поиска нименьшего элемента массива.

def findSmallest(arr):
    smallest = arr[0]       # for saving the least value
    smallest_index = 0      # for saving the index of the least value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


print(findSmallest([4, 2, 1, -6, -1, 13]))