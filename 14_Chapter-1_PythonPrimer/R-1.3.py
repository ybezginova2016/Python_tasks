# R-1.3
# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    sor = sorted(data)
    smallest = sor[0]
    largest = sor[-1]
    return smallest, largest

data = [1, 2, 6, 99]
print(minmax(data))

def minmax2(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest


alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]
print(minmax2(alpha))


