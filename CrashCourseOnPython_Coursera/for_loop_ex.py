# 1
for x in range(5):
    print(x)

"""
1) In Python a range of numbers will start with
the value0 by default.

2) The list of numbers generated will be one
less than the given value.
"""
# 2
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print('Hi ' + friend)

# 3
values = [23, 52, 58, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print('Total sum: ' + str(sum)+ ' - Average: ' + str(sum/length))
print()

# 4
def to_celsius(x):
    return round((x-32)*5/9, 2)

for x in range(0, 101, 10):
    print(x, to_celsius((x)))