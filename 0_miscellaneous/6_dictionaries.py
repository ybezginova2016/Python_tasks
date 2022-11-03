A = [['Vienna', 'Austria'],
     ['Belgrade', 'Serbia'],
        ['Moscow', 'Russia']]

me = dict(A)
print(me)

me['Berlin'] = 'Germany'
print(me)
print()

for d in me.keys():
    print('City:', d)
    print('Country:', me[d])

girls = {
    ('B', 'C', 'C') : 'Sveta',
    ('C', 'D', 'B') : 'Mara',
    ('A', 'B', 'A') : 'Yulia'
}

print(girls)
# Обращение к элементу словаря по ключу
print(girls[('B', 'C', 'C')])

for g in girls.keys():
    print('Score:', g)
    print('Name:', girls[g])