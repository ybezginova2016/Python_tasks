# Cheat Sheet: List Methods

# Method 1 - lst.append(x)
#  Appends element x to the list 'lst'.
l = []
l.append(42)
l.append(12)
l.append('Yulia')
print(l)

# Method 2 - lst.clear()
# Removes all element from the list lst-which becomes empty.
rem = [1, 3, 4, 5, 6, 'Yulia']
rem.clear()
print(rem)

# Method 3 - lst.copy()
# Returns a copy of the list lst. Copies only the list, not the
# elements in the list (shallow copy)
a = [1, 3, 5]
a.copy()
print(a)

# Method 4 - lst.count(x)
# Counts the number of occurrences of element x in the list lst.
b = [1, 6, 5, 13, 5, 5, 'Yulia', 7]
print(b.count(43))
print(b.count(5))
print(b.count('Yulia'))

# Method 5 - lst.extend(iter)
# Adds all the elements of an iterable iter (e.g., another list) to the list.
c = [1, 5, 'Yulia']
c.extend('BGI')
c.extend(['BGI'])
print(c)

# Method 6 - lst.index()
# Returns the position (index) of the first
# occurence of the value x in the list lst.
d = [1, 5, 'Yulia']
print(d.index('Yulia'))

# Method 7 - lst.insert(i, x)
# Insert element x at position (index) i in the list lst.
e = [99, 1, 13, 'Yulia', 99, 123, 12, 'Yulia']
print(e.index('Yulia'))
print(e.index(99))
print(e.index(13))

# Method 8 - lst.pop()
# Removes and returns the final element of the list lst
f = [1, 4, 5, 6]
f.pop()
print(f)

# Method 9 - lst.remove(x)
# Removes and returns the first occurence of element x in the list lst
g = [1, 4, 7, 8]
g.remove(7)
print(g)

# Method 10 - lst.reverse()
# Reverses the order of elements in the list lst.
m = [1, 13, 6, 7]
m.reverse()
print(m)

# Method 11 - lst.sort()
# Sorts the elements in the list lst. in ascending order.
n = [134, 989723, 23402398, 2342, 124545, 99, 120]
n.sort()
print(n)