# R-1.5
# Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.

def sum_of_squares(n):
    arr = []
    for i in range(0, n):
        arr.append(i * i)
    return sum(arr)

print(sum_of_squares(4))

def sum_of_sq(n):
    return sum([i * i for i in range(0, n)])

print(sum_of_sq(4))
