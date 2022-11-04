name = 'Bob'
age = 25

string = 'Hi, my name is %s and I am %i years old!' % (name, age)
print(string)

string1 = f'Hello, { name }!'
print(string1)

string2 = f'1 + 1 is { 1 + 1}'
print(string2)

quantity = 100
total = 2.423523523 * quantity
price_per_liter = total / quantity
print('Quantity: %d Total: %.2f' % (quantity, total))
print('%.5f' % price_per_liter)

title1 = 'Quantity'
title2 = 'Price'
print('%10s %10d' % (title1, 24))
print('%10s %10d' % (title2, 17.29))
print()
print('%10s %10d' % (title1, 24))
print('%10s %10.2f' % (title2, 17.29))
