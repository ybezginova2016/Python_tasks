"""
R-1.11
Demonstrate how to use Python’s list comprehension
syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
a = [2 ** k for k in range(0, 9, +1)]
print(a)