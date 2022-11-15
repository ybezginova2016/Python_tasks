###### EXERSISE 1 ######
# Функция выбрана так, что её минимум находится в точке (1.5, -0.5).

# Мы записали функцию f, в коде назвали её func(). Напишите функцию
# gradient(), которая по формуле вычисляет её градиент.
# Проверьте эту функцию на нескольких векторах.

import numpy as np

def func(x):
    return (x[0] + x[1] - 1)**2 + (x[0] - x[1] - 2)**2

def gradient(x):
    return np.array([4 * x[0] - 6,
                    4 * x[1] + 2
                    ])

print(gradient(np.array([0, 0])))
print(gradient(np.array([0.5, 0.3])))

# Направление наискорейшего роста функции меняется при переходе от
# одной точки к другой.

###### EXERCISE 2 ######
# Функция выбрана так, что её минимум находится в точке (1.5, -0.5).

# Напишите функцию gradient_descent(), реализующую алгоритм
# градиентного спуска для функции f(x). На вход она принимает:

# initialization — начальное значение вектора x;
# step_size — размер шага μ;
# iterations — количество итераций.

# Функция возвращает значение вектора x после заданного числа
# итераций. Проверьте функцию на разных количествах итераций.

import numpy as np

def func(x):
    return (x[0] + x[1] - 1)**2 + (x[0] - x[1] - 2)**2

def gradient(x):
    return np.array([4 * x[0] - 6, 4 * x[1] + 2])

def gradient_descent(initialization, step_size, iterations):
    x = initialization
    for i in range(iterations):
        x = x - step_size * gradient(x)
    return x

print(gradient_descent(np.array([0, 0]), 0.1, 5))
print(gradient_descent(np.array([0, 0]), 0.1, 100))