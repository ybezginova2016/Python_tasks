def foo(a, b=15, c=27):
    return a, b, c

print(foo(a=1333))

"""
In this case, the built-in abs function is itself sent as the
value associated with the keyword parameter key. (Functions are 
first-class objects
in Python; see Section 1.10.) When max is called in this way, 
it will compare abs(a)
to abs(b), rather than a to b.
"""
a = - 35
b = 20
print(max(a, b, key=abs))
print(max(a, b))
