import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.mean()) # 2.5
print(arr.sum()) # 10

import numpy as np

X = np.array([[2, 1], [4, 1], [7, 1]])
w = np.array([-0.25, 7.5])
y = np.array([6, 8, 5])

# Расчёт невязок.
e = y - X @ w
print(e)

# Первый способ — разделить сумму на количество точек.
l_1 = abs(e).sum() / len(e)
print(l_1)

# Второй способ — сразу посчитать среднее с помощью метода .mean().
# Более предпочтителен, так как короче и легче читается.
l_1 = abs(e).mean()
print(l_1)

# Первый способ — разделить сумму на количество точек.
l_2 = (abs(e).sum())**2 / len(e)
print(l_2)

# Второй способ — сразу посчитать среднее с помощью метода .mean().
# Более предпочтителен, так как короче и легче читается.
l_2 = (abs(e)**2).mean()
print(l_2)

# Упражнение 3
# Рассчитайте MSE и MAE для заданных точек и прямой.
# Подсчитанные значения сохраните в переменных mse и mae
# соответственно. Выведите их значения.

import numpy as np
X = np.array([[2, 1], [3, 1], [4, 1], [2.5, 1], [3.5, 1]])
w = np.array([-0.5, 3])
y = np.array([1, 3, 2, 4.5, 3])

# Расчёт невязок.
e = y - X @ w
print(e)

# Первый способ — разделить сумму на количество точек.
mae = abs(e).sum() / len(e)
print(mae)

# Второй способ — сразу посчитать среднее с помощью метода .mean().
# Более предпочтителен, так как короче и легче читается.
mae = abs(e).mean()
print(mae)

# Первый способ — разделить сумму на количество точек.
mse = (abs(e).sum())**2 / len(e)
print(mse)

# Второй способ — сразу посчитать среднее с помощью метода .mean().
# Более предпочтителен, так как короче и легче читается.
mse = (abs(e)**2).mean()
print(mse)

# Для подсчёта норм используем функцию np.linalg.norm . Она ожидает на вход два параметра: вектор и номер нормы, которую нужно рассчитать.
# Код рассчитывает MAE. Измените код, чтобы рассчитать MSE.
import numpy as np

X = np.array([[2, 1], [4, 1], [7, 1]])
w = np.array([-0.25, 7.5])
y = np.array([6, 8, 5])

# Расчёт невязок.
e = y - X @ w
print(e)

# Подсчёт ошибки первым подходом.
l_1 = abs(e).mean()
print(l_1)

# Подсчёт ошибки через норму.
l_1 = np.linalg.norm(e, 1) / len(e)
print(l_1)

# Подсчёт ошибки первым подходом.
l_2 = (abs(e)**2).mean()
print(l_2)

# Подсчёт ошибки через норму.
l_2 = (np.linalg.norm(e, 1)**2) / len(e)
print(l_2)

print()
#### EXERCISE ####

import numpy as np
X = np.array([[1, -1], [3, 1], [4, 1], [9, 1]])
w = np.array([0.36, 1.9])
y = np.array([-1, 2, 10, 3])

# Расчёт невязок.
e = y - X @ w
print(e)

# Первый способ — разделить сумму на количество точек.
mae = abs(e).sum() / len(e)
print("MAE y1: {}".format(mae))

# Второй способ — сразу посчитать среднее с помощью метода .mean().
# Более предпочтителен, так как короче и легче читается.
mae = abs(e).mean()
print("MAE y1: {}".format(mae))

# Первый способ — разделить сумму на количество точек.
mse = (abs(e).sum())**2 / len(e)
print("MSE y1: {}".format(mse))

# Второй способ — сразу посчитать среднее с помощью метода .mean().
# Более предпочтителен, так как короче и легче читается.
mse = (abs(e)**2).mean()
print("MSE y1: {}".format(mse))

print()

import numpy as np

X = np.array([[1, -1], [3, 1], [4, 1], [9, 1]])
w = np.array([0.17, 1.5])
y = np.array([-1, 2, 10, 3])

# Расчёт невязок.
e = y - X @ w
print(e)

# Подсчёт ошибки первым подходом.
l_1 = abs(e).mean()
print(l_1)

# Подсчёт ошибки через норму.
l_1 = np.linalg.norm(e, 1) / len(e)
print(l_1)

# Подсчёт ошибки первым подходом.
l_2 = (abs(e)**2).mean()
print(l_2)

# Подсчёт ошибки через норму.
l_2 = (np.linalg.norm(e, 1)**2) / len(e)
print(l_2)

##### EXERCISE #####
print()
# Задача 3
# Рассчитайте невязки для набора точек и прямой. Сохраните
# рассчитанный вектор в переменной result и выведите её.
import numpy as np
X = np.array([[-1, 1], [4, 1], [4, 1], [8, 1], [10, 1]])
y = np.array([0, 4, 6, 8, 12])
w = np.array([1, 0.85])

# Расчёт невязок.
result = y - X @ w
print(result)
print()

##### EXERCISE #####
# Задача 4
# Рассчитайте MSE и MAE для заданных точек и прямой. Подсчитанные
# значения сохраните в переменных mse и mae соответственно.
# Выведите их.
import numpy as np
X = np.array([[-1, 1], [4, 1], [4, 1], [8, 1], [10, 1]])
y = np.array([0, 4, 6, 8, 12])
w = np.array([1, 0.85])

# Расчёт невязок.
e = y - X @ w
print(e)
print()

# Подсчёт ошибки первым подходом.
mae = abs(e).mean()
print(mae)

# Подсчёт ошибки через норму.
mae = np.linalg.norm(e, 1) / len(e)
print(mae)

# Подсчёт ошибки первым подходом.
mse = (abs(e)**2).mean()
print(mse)

# Подсчёт ошибки через норму.
mse = (np.linalg.norm(e, 1)**2) / len(e)
print(mse)