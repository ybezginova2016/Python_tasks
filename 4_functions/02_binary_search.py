# Бинарный поиск

# При бинарном поике каждый раз отсекается половина чисел

# Бинарный поиск работает только в том случае, если список отсортирован.
# Функиця б/п binary_search получает отсортированный массив и значение.
# Если значение присутствует в массиве, то функция возвращает его позицию.
# При этом мы должны следить за тем, в какой части массива
# проводится поиск.

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 3, 4, 13, 31]

print(binary_search(my_list, 3))
print(binary_search(my_list, 0))
print(binary_search(my_list, 32))
