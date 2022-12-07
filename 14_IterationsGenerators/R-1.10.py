"""
R-1.10 What parameters should be sent to the range constructor, to
produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
"""

### option 1 ###
a = list(range(8, -1, -2))
b = list(range(-8, -1, +2))
print(a)
print(b)

final = a + b
print(final)

### option 3 ###
fin = list(range(8, -1, -2)) + list(range(-8, -1, +2))
print(fin)

### option 2 ###
print(list(range(8, -10, -2)))