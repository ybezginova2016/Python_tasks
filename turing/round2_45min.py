########## Turing Test 17-12-2022 ###########
class Developer(object):
    def __init__(self, skills):
        self.skills = skills
    def __add__(self, other):
        skills = self.skills + other.skills
        return Developer(skills)
    def __str__(self):
        return "Skills"

A = Developer('NodeJS')
B = Developer('Python')

#####################
x = ['ab', 'cd']
print(list(map(lambda x:len(x), x)))

#####################
array = ['Welcome', 'To', 'Turing']
print('-'.join(array))
print('Welcome to TURING'.capitalize())

#####################
arr1 = [1, 2 ,3 ,4, 5]
arr2 = arr1
arr2[0] = 0
print(arr1)

#####################
inputs = ['nodejs', 'reactjs', 'vueljs']
print(inputs)

for i in inputs:
    inputs.append(i.upper())

print(inputs)

#####################
try:
    print('Hello')
except:
    print('abc')
finally:
    print('World')

#####################
t = '%(a)s'
print(t % dict(a = 'Welcome',
                b = 'to',
                c = 'Turing'))

#####################
def func1():
    x = 50
    return x
print(func1())
print(x)

#####################
def listSkills(val, list=[]):
    list.append(val)
    return list
l1 = listSkills('NodeJA')
l2 = listSkills('NodeJAS')
print('%s' % l1)
print('%s' % l2)

#####################
z = set('abc')
z.add('san')
z.update(set(['p', 'q']))
print(z)

data = [10, 20, 30, 40, 50]
data.pop()
print(data)
data.pop(2)
print(data)

#####################
import re
result = re.findall('Welcome to Turing', 'Welcome', 1)
print(result)

#####################
x = 'abcdef'
i = 'a'
while i in x[:-1]:
    print(i, end=' ')

#####################
f = None

for i in range(5):
    with open('app.log', 'w') as f:
        if i > 2:
            break

print(f.closed)
#####################
l = [1, 2, 3, 4, 5]
m = map(lambda x: 2 ** x, l)
print(list(m))

#####################
alph = 'abcd'
for i in range(len(alph)):
    alph[i].upper()

print(alph)

######## returns ERROR #############

# Y = [2, 5J, 6]
# Y.sort()
# print(Y)

#####################
a = [1, 2, 3, 4]
b = [sum(a[0:x+1]) for x in range(0, len(a))]
print(b)