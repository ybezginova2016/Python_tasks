class SimpleClass:
    # class attribute
    i = '12345'

print(SimpleClass.i)
o1 = SimpleClass()
o2 = SimpleClass()
print(o1.i)

o1.name = 'Object1'
o2.name = 'Object2'

print(o1.name)
print(o2.name)

o1.i = 'o1.i'
print(o1.i)
print(SimpleClass.i)

print(o2.i)
