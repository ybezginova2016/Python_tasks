"""
O(log(n))

Каждый элемент массива на самом деле состоит из двух элементов: названия
товара и его цены . Если отсортировать массив по имени, вы сможете
провести по нему бинарный поиск для определения цены товара. Это означает,
что поиск будет выполняться за время O(log п).

Bisecton / Binary Search

- When a list is sorted, we can divide the search scope in two
at every step in the search process

- This will save time in comparison to linear search at the cost of
a single sort initially

- Every time the list is divided into two parts, the problem size is
halved.

"""
def search(l, e):
    def bisect(start, end):
    # when end == start, range is empty
    if end == start:
        return None

    # number of elements in range is (end - start)
    count = end - start
    # mid is half of count form the start
    mid = start + count // 2

    # check which half of the list we shoulf look in
    if l[mid] > e:
        return bisect(start, mid)
    elif l[mid] < e:
        return bisect(mid + 1, end)

    # only other possibility is that the element in the middle
    # is the one we are looking for
        return mid
# use the helper function to find the index of the value
    return bisect(0, len(l))

# def f2(x):
#     return (x + 1) * math.log10(x) - x ** 0.75
# print(search(f2, 0.000001))
