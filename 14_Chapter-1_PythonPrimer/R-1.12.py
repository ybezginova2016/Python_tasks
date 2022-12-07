"""
For more: https://github.com/reversegremlin/pythagoras/blob/master/primer.py

R-1.12 Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""
import random
def my_choice(iterable):
    index = random.randrange(0, len(iterable)-1)
    return iterable[index]

print(my_choice([1, 6, -5, -100]))