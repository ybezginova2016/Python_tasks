# Python supports similar comprehension syntaxes that respectively produce a
# set, generator, or dictionary. We compare those syntaxes using our example for
# producing the squares of numbers.
# [ k*k for k in range(1, n+1) ] list comprehension
# { k*k for k in range(1, n+1) } set comprehension
# ( k*k for k in range(1, n+1) ) generator comprehension
# { k : k*k for k in range(1, n+1) } dictionary comprehension

# option 1
n = 3
squares = []
for k in range(1, n+1):
    squares.append(k*k)

print(squares)

# option 2 - comprehension
squares2 = [k*k for k in range(1,n+1)]
print(squares2)

##########################
# option 1
factors = [k for k in range(1,n+1) if n % k == 0]
print(factors)

# option 2
factors2 = []
for k in range(1,n+1):
    if n % k == 0:
        factors2.append(k)

print(factors2)
