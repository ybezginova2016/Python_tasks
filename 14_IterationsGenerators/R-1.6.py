# R-1.6 (page 51)
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the [odd] positive integers smaller than n.

def positive_int(n):
    # n -= 1 # --> if while loop
    sum_of_sq = 0
    for i in range(0, n):
        sum_of_sq += i * i if i & 1 == 1 else 0
    return sum_of_sq

print(positive_int(5))

def is_even2(k):
    # bitwise-and
    # 1 & 1 = 1 odd, 0 & 1 = 0 even
    return False if k & 1 else True

print(is_even2(76))


#### easy option ####
def sum_of_squares_odd(n):
    n -= 1
    total = 0
    while n > 0:
        if n % 2 != 0:
            total += n * n
        n -= 1
    return total

print(sum_of_squares_odd(6))