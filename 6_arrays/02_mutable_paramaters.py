def remove_all(lst, value):
    while value in lst:
        lst.remove(value)
    return lst

print(remove_all([5, 4, 1, 6, 8, 3, 1, 4, 2, 1, 1, 1, 1, 1, 5], 1))