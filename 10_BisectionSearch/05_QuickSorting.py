# O(n log(n))

# Разделяй и властвуй

# Просуммировать все числа и вернуть сумму (в цикле)
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1, 6, 4, 2, 13]))

# Просуммировать все числа и вернуть сумму (рекурсией)
# 1) определить базовый случай
# 2) свести задачу к базовому случаю

def sum_re(arr):
    if arr == []:
        return 0
    else:
        # pop() removes the element at the specified position
        return arr.pop(len(arr) - 1) + sum_re(arr)
print(sum_re([1, 6, 4, 2, 13]))

# The pop() method removes the element at the specified position.
fruits = ['apple', 'banana', 'cherry']
print(fruits.pop(1))
print(fruits)

# Быстрая сортировка

def quicksort(array):
    # Базовый случай
    if len(array) < 2:
        return array
    # Рекурсивный случай
    else:
        pivot = array[0]
        # подмассив всех элементов, меньших опорного
        less = [i for i in array[1:] if i <= pivot]
        # подмассив всех элементов, больших опорного
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

# Мы используем стратегию «разделяй и властвуй» . Следовательно,
# массив должен разделяться до тех пор, пока мы не придем к базовому
# случаю.
#
# Алгоритм быстрой сортировки работает так: сначала в массиве
# выбирается элемент, который называется опорным.

print(quicksort([13, 1, 5, 2, 112, 11, 13]))

# O(n)
# def print_items(list):
#     for item in list
#         sleep(1)
#         print(item)