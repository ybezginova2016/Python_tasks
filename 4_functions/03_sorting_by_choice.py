# Напишем функцию сортировки выбором

from _03_array_sorting  import findSmallest         # importing function from other file
def selectorSort(arr):                      # sorting the array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)        # searching for the least value
        newArr.append(arr.pop(smallest))    # pop(smallest) - удалить число smallest из исходного массива
    return newArr

print(selectorSort([4, 5, -13, 0, 1, 2]))