import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0, 1], [8, 1], [0, 1], [8, 1]])
y = np.array([10, 7, 7, 6])

# Рассчитываем коэффициенты прямой по формуле.
# w - вектор коэффициентов [k, m].
w = np.linalg.inv(X.T @ X) @ X.T @ y

# Также можно сохранить коэффициенты сразу в отдельные переменные.
k, m = np.linalg.inv(X.T @ X) @ X.T @ y

# Рассчитать предсказание для произвольной точки можно по формуле прямой.
x_test = 6
y_pred = w[0] * x_test + w[1]
print(f"Продуктивность через {x_test} часа(ов) после начала смены:")
print(y_pred)

# Код для построения графика, его можно не изменять.
for i in range(len(y) // 2):
    plt.scatter(X[i::2, 0], y[i::2], s=100, label=f"День {i+1}")
plt.scatter(x_test, y_pred, zorder=10, s=100, label="Тестовая точка (x_test, y_pred)")

x_min = -1; x_max = 9
y_min = x_min * w[0] + w[1]
y_max = x_max * w[0] + w[1]

plt.plot(
    [x_min, x_max],
    [y_min, y_max],
    linewidth=3,
    c="C4",
    label="Наилучшая прямая",
)
plt.grid()
plt.ylim(-1, 11.5)
plt.xlim(-1, 9)
plt.ylabel("😊", rotation=0, fontsize=25, labelpad=20)
plt.xlabel("Часы после начала смены, t", fontsize=15)
plt.legend(loc=3)
plt.show()

###### EXERCISE 2 ######
# Упражнение 2
# Рассчитайте коэффициенты оптимальной прямой для заданных точек.
# Вектор коэффициентов сохраните в переменной w. Сделайте
# предсказание для x = 1.5.x=1.5. Результат сохраните в переменной
# result.
import numpy as np
import matplotlib.pyplot as plt
X = np.array([[2, 1], [3, 1], [4, 1], [2.5, 1], [3.5, 1]])
y = np.array([1, 3, 2, 4.5, 3])

# Рассчитываем коэффициенты прямой по формуле.
# w - вектор коэффициентов [k, m].
w = np.linalg.inv(X.T @ X) @ X.T @ y

# Также можно сохранить коэффициенты сразу в отдельные переменные.
k, m = np.linalg.inv(X.T @ X) @ X.T @ y

x_test = 1.5
result = w[0] * x_test + w[1]
print(result)

# Код для построения графика, его можно не менять.
x_min = 1; x_max = 5
y_min = x_min * w[0] + w[1]
y_max = x_max * w[0] + w[1]

plt.scatter(X[:, 0], y, s=100)
plt.vlines(x_test, 0, 5, linestyle='--', color='C1', label="Тестовая точка x_test")
plt.scatter(x_test, result, zorder=10, s=100)

plt.plot(
    [x_min, x_max],
    [y_min, y_max],
    linewidth=3,
    c="C1",
)
plt.xlabel("$x$", fontsize=15)
plt.ylabel("$y$", fontsize=15, rotation=0, labelpad=15)
plt.xlim(x_min, x_max)
plt.ylim(0, 5)
plt.grid()
plt.show()

# Формула, которую мы получили, позволяет по заданному набору точек
# построить прямую и использовать её для получения предсказаний
# в новых точках. Мы рассмотрели пример с точками на плоскости,
# и эту же формулу можно использовать при работе с данными
# бо́льшей размерности.