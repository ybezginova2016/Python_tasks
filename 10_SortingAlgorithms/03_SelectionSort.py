# O(n^2)
# Напишем функцию для поиска наименьшего элемента массива
# Сортировка массива по возрастанию
def findSmallest(arr):
    # storing a min value
    smallest = arr[0]
    # storing an index of the smallest value
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
    return smallest_index

print(findSmallest([400, 15, 13, 99]))

# Поиска наименьшего значения сортировкой выбором
def selectionSort(arr): # sorting an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([400, 15, 13, 99]))