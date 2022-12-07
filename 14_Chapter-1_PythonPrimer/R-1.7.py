"""
R-1.7
Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function.
"""

def sum_of_sq(n):
    return sum([i * i for i in range(0, n) if i % 2 != 0])

print(sum_of_sq(5))