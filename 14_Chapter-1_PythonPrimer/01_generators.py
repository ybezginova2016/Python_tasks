def factors(n):
    results = []                # store factors in a new list
    for k in range(1, n+1):
        if n % k == 0:          # divides evenly, thus k is a factor
            results.append(k)   # add k to the list of factors
    return results              # return the entire list

print(factors(5))

# In contrast, an implementation of a generator for computing those factors could be
# implemented as follows:

def factors2(n):            # generator that computes factors
    for k in range(1,n+1):
        if n % k == 0:      # divides evenly, thus k is a factor
            yield k         # yield this factor as next result

print(list(factors2(5)))

# Notice use of the keyword yield rather than return to indicate a result. This indicates
# to Python that we are defining a generator, rather than a traditional function. It
# is illegal to combine yield and return statements in the same implementation, other
# than a zero-argument return statement to cause a generator to end its execution. If
# a programmer writes a loop such as for factor in factors(100):, an instance of our
# generator is created. For each iteration of the loop, Python executes our procedure
# until a yield statement indicates the next value. At that point, the procedure is temporarily
# interrupted, only to be resumed when another value is requested. When
# the flow of control naturally reaches the end of our procedure (or a zero-argument
# return statement), a StopIteration exception is automatically raised.

def factors3(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

print(list(factors3(5)))

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        future = a + b
        a = b
        b = future

print(list(fibonacci()))