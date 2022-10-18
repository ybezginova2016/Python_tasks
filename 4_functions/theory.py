"""
Defining Functions Recap
We looked at a few examples of built-in functions in Python,
but being able to define your own functions is incredibly powerful.
We start a function definition with the def keyword, followed
by the name we want to give our function. After the name,
we have the parameters, also called arguments, for the function
enclosed in parentheses. A function can have no parameters,
or it can have multiple parameters. Parameters allow us to call
a function and pass it data, with the data being available inside
the function as variables with the same name as the parameters.
Lastly, we put a colon at the end of the line.

After the colon, the function body starts. It’s important to note
that in Python the function body is delimited by indentation.
This means that all code indented to the right following a function definition is part of the function body. The first line that’s no longer indented is the boundary of the function body. It’s up to you how many spaces you use when indenting -- just make sure to be consistent. So if you choose to indent with four spaces, you need to use four spaces everywhere in your code.

"""

# определим функцию
def drawBox():
    print("**********")
    print("* *")
    print("* *")
    print("**********")

# вызов функции
drawBox()

# 4.1. Функции с параметрами

## Рисуем прямоугольник из звездочек, заполненный пробелами
# @param width – ширина прямоугольника
# @param height – высота прямоугольника

def drawBox(width, height):
    # Слишком маленькие прямоугольники не могут быть
    # нарисованы при помощи этой функции
    if width < 2 or height < 2:
        print("Ошибка: ширина или высота прямоугольника слишком малы.")
        quit()
    # Рисуем верхнюю линию прямоугольника
    print("*" * width)
    # Рисуем стороны прямоугольника
    for i in range(height - 2):
        print("*" + " " * (width - 2) + "*")
# Рисуем нижнюю линию прямоугольника
    print("*" * width)

drawBox(6, 4)

# drawing rectangule
# @param width
# @param height
# @param outline - символ для рисования сторон прямоугольника
# @param fill - символ для заливки прямоугольника

def drawBox(width, height, outline="*", fill=" "):
    if width < 2 or height < 2:
        print("Ошибка: ширина или высота прямоугольника слишком малы")
        quit()
    print(outline * width)
    for i in range(height - 2):
        print(outline + fill * (width - 2) + outline)
    print(outline * width)

drawBox(13, 6, "@", ".")

print()

"""
1) Находить минимум производльного количества аргументов
min(-6, 12, 13)

2) Использовать функцию min для кортежей, списоков, множеств и других последовательностей
xs = {-6, 12, 13}
min (???)

3) Ограничить минимум произвольным отрезком [lo, hi]
bounded_min(-6, 12, 13, lo=0, hi=255)

4) По заданным lo, hi строить функцию bounded min
bounded_min = make_min(lo=0, hi=255)
bounded_min(-5, 12, 13)
"""
# Упаковка аргументов

def min(*args): #type(args) == tuple
    res = float("inf")
    # поддерживаем текущий минимум, инициализируя его бесконечностью
    for arg in args:
        if arg < res:
            res = arg
    return res

print(min(-6, 12, 13))

# Как потребовать, чтобы в args был хотя бы один элемент?

def min(first, *args): #type(args) == tuple
    res = first
    # поддерживаем текущий минимум, инициализируя его бесконечностью
    for arg in args:
        if arg < res:
            res = arg
    return res

print(min(-6, 12, 13))

# Как применить функцию min к коллекции? Применить ситнтаксис, симметричный упаковке, - распаквока.
# РАСПАКОВКА ЭЛЕМЕНТОВ

# Синтаксис будет работать с любым объектом, поддерживающим протокол итератора.
def min(*xs): #type(args) == tuple
    res = float("inf")
    # поддерживаем текущий минимум, инициализируя его бесконечностью
    for arg in xs:
        if arg < res:
            res = arg
    return res

print(min(*{-6, 12, 13}))
print(min(*[-6, 12, 13]))
print(min(*(-6, 12, 13)))
print()
# Распаковывать сет - странная идея.

# Ключевые аргументы: аргументы по умолчанию

def bounded_min(first, *args, lo=float("-inf"), hi=float("inf")):
    res = hi
    for arg in (first, ) + args:
        if arg < res and lo < arg < hi:
            res = arg
    return max(res, lo)

print(bounded_min(-6, 12, 13, lo=0, hi=255))
# args = tuple
# (first, ) - это одноэлементный кортеж
print()

# В какой момент происходит инициализация ключевых аргументов со значениями по умолчанию?
# В момент инциализации байт-кода 1 раз.

def unique(iterable, seen=set()):
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc

xs = [1, 1, 2, 3, 5]
print(unique(xs))
print(unique(xs)) # будет пустой список, так как значение аргумента по умолчанию инициализируется ровно один раз -
# в момент компиляции в байт-код
# абсолютно все вызовы функции unique() будут разделять значения атрибута seen

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
bigger, smaller = order_numbers(100, 99)
print(smaller, bigger)
###########################################
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is {}".format(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
round_trip = my_trip_km*2
print("The round-trip in kilometers is {}", format(round_trip))

###################2###################
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
bigger, smaller = order_numbers(100, 99)
print(bigger, smaller)

###################4###################

def lucky_number(name):
    number = len(name) * 9
    result = "Hello " + name + ". Your lucky number is " + str(number)
    return result


print(lucky_number("Kay"))
print(lucky_number("Cameron"))

###################5######################
# Вопрос 5
# If a filesystem has a block size of 4096 bytes,
# this means that a file comprised of only one byte
# will still use 4096 bytes of storage. A file made
# up of 4097 bytes will use 4096*2=8192 bytes of storage.
# Knowing this, can you fill in the gaps in the
# calculate_storage function below, which calculates
# the total number of bytes needed to store a file of
# a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = 4097
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = full_blocks % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 2
    return 1

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

###############################################
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))