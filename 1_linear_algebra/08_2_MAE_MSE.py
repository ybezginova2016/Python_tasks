# Особенности использования MAE и MSE

# В учебниках и статьях функция MSE встречается чаще, чем MAE.

# Одна из причин этого — так сложилось исторически.
# В XVIII–XIX веках появились первые математические работы
# в направлении анализа данных. В то время существовали вычислительные
# алгоритмы, позволяющие найти минимум дифференцируемой функции.
# Удобных методов найти минимум недифференцируемой функции в то
# время не было.

# Функция MSE представляет собой сумму квадратов, значит, как раз
# является дифференцируемой. Поэтому её минимум легко найти с
# помощью производной. MAE представляет собой сумму модулей,
# модуль имеет излом, в котором производная функции не существует.

# Из-за этого появлялись сложности при применении стандартных
# алгоритмов поиска точки минимума.
# Поэтому достаточно долго для предсказания данных использовали
# минимизацию только функции MSE.
# Сейчас уже есть удобные вычислительные алгоритмы, которые
# позволяют найти минимум недифференцируемой функции.
# Так что можно найти минимум функции MAE с точностью,
# достаточной для практических нужд. Обычно выбор функции
# ошибки происходит в зависимости от специфики задачи и
# особенностей самих функций MAE и MSE.

# Задача 2
# Рассчитайте коэффициенты оптимальной прямой для заданных точек.
# Сохраните вектор коэффициентов в переменной w. Сделайте предсказание
# для x = 6.x=6. Результат сохраните в переменной result и выведите
# на экран.

import numpy as np
X = np.array([[-1, 1], [4, 1], [4, 1], [8, 1], [10, 1]])
y = np.array([0, 4, 6, 8, 12])
w = np.linalg.inv(X.T @ X) @ X.T @ y
x_test = 6

result = w[0] * x_test + w[1]
print(result)
print(w)

# Задача 3
# Рассчитайте наилучшие веса для заданного набора точек в многомерном
# пространстве. Сохраните полученные веса в переменной w. Получите
# предсказание для точки x_test, сохраните его в переменной result.
# Выведите на экран полученные значения w и result.

import numpy as np

X = np.array(
    [
        [ 2,  1,  1],
        [ 2, -4,  1],
        [ 0, -3,  1],
        [ 1, -4,  1],
        [-2, -5,  1],
        [-3, -1,  1]
	]
)

y = np.array(
	[
        0.79360363,
        4.12033812,
        5.08632068,
        8.02628284,
        8.93128108,
        9.73436965
	]
)

x_test = [1, -2, 1]

w = np.linalg.inv(X.T @ X) @ X.T @ y

result = x_test @ w

print(result)
print(w)

##### np.stack #####
import numpy as np

# Исходные векторы.
A = np.array([1, 2])
B = np.array([3, 4])

print("Исходные векторы:")
print(f"A: {A}")
print()
print(f"B: {B}")
print()


# Склейка по вертикали. Попробуйте изменить строку ниже.
print(np.stack([A, B], axis=0))
print()
print(np.stack([B, A], axis=0))
print()
print(np.stack([A, B], axis=1))
print()
print(np.stack([B, A], axis=1))
