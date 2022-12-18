# EX 1
inc_count = '2256'
print(type(inc_count))
print(inc_count)

inc_count = int(inc_count)
print(type(inc_count))
print(inc_count)

# EX 2
# txt = 'Python'
# txt[2], txt[1] = txt[1], txt[2]
#
# print(txt) # returns TypeError: 'str' object does not support item assignment

# EX 3
a, b = [0], [0]
a, b = b, a
print(a is b)

# EX 4
# def foo(a=[]):
#     print(a)
#
# foo.__defaults__[0] = 1 # TypeError: 'tuple' object does not support item assignment
# print(foo())

# # EX 5
# lst = [1, 2, 3, 4, 5]
# lst[::2] = range(4) # ValueError: attempt to assign sequence of size 4 to extended slice of size 3
# # python-BaseException
# print(lst)

# EX 6
class Foo(object):
    def __eq__(self, other):
        return True
print(Foo() == None)

# EX 7
print(print('py'))

# EX 8
def exists_num(l, to_find):
    for num in l:
        if num == to_find:
            print(1)
            return
        else:
            print(2)

lst = [1, 2, 3]
exists_num(lst, 0)
exists_num(lst, 1)

# EX 9
def combine_lists(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a < len_b:
        limit = len_a

    else:
        limit = len_b
    i = 0
    r = []

    while i < limit:
        r.append(a[i])
        r.append(b[i])
        i += 1
    return r

if __name__ == '__main__':
    a = ['a', 'c']
    b = ['A', 'C', 'D']
    print(repr(combine_lists(a, b)))

# EX 10
s = {range(4)}
print(s)