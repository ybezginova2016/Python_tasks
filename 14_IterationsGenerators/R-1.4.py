# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def positive_func(n):
    # n = n - 1
    n -= 1
    sum_res = 0

    while n > 0:
        sum_res += n * n
        n -= 1
    return sum_res

print(positive_func(5))