# R-1.5
# Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.

def sum_of_squares(n):
    for i in range(0, n):
        sq = i * i
        res = sum(sq)
        i += 1
    return res

print(sum_of_squares(4))
