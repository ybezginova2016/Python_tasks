# Lists
my_list = [10, 20, 30]
for i in my_list:
    print(i)
# List comprehension
my_lt = [n for n in range(1, 21)]
print(my_lt)

for i in my_lt:
    print(i)

# Tuples
my_tup = (1, 2, 3, 4, 6, 7, 8)
for i in my_tup:
    print(i)

# Dict
my_dict = {'name' : 'Jake',
           'age' : 21,
           'occupation': 'Data Scientist'
           }
print(my_dict)

for key, val in my_dict.iteritems():
    print('My {} is {}'.format(key, val))

print("Age 21 is of:", my_dict['age'])

my_dict['name'] = 'Yulia'
my_dict['age'] = 32

print(my_dict)