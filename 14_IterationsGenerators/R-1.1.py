# R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

print(is_multiple(5, 6))
print(is_multiple(36, 6))
