# Write a iterative and recursive function that mimplements
# the factorial of a number.

### ITERATIVE APPROACH ###

n = 4
def fact_iter(n):
    # the variable that stores the multiplications
    x = 1
    for i in range(n, 0, -1):
        # x = x * i
        x *= i
    return x

print(fact_iter(n))

### RECURSIVE APPROACH ###
def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)

print(fact_recur(n))
