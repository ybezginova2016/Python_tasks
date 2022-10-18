def remove_all(lst, value):
    while value in lst:
        lst.remove(value)
    return lst

print(remove_all([5, 4, 1, 6, 8, 3, 1, 4, 2, 1, 1, 1, 1, 1, 5], 1))

print()

def mystery(s, lst):
    s = s.upper() # upper creates a new string
    lst = lst + [2]
    return lst

s = 'a'
lst = [1]
print(s, lst)

# Using + with lists creates a new list (it doesn’t change
# an existing list!), so this makes the local variable lst
# refer to the new list: [1, 2].
# But, again, it hasn’t changed what lst refers to
# outside of the function; it’s still [1].
print()
def mystery(s, lst):
    s = s.upper() # upper creates a new string
    lst = lst + [2]
    lst.append(2)

s = 'a'
lst = [1]
print(s, lst)
print()
def func():
    for i in range(10):
        for j in range(10):
            print(i, j)
            if j == 4:
                return

# return это безусловный оператор выхода из функции,
# break это оператор остановки цикла
# Если ты напишешь break ты выйдешь только из Нижнего цикла
# и попадёшь на верхний

func()
print()
def no_high(lst):
    for card in lst:
        if card in ['jack', 'queen', 'king', 'ace']:
            return False
        else:
            return True

print(no_high(['blue']))