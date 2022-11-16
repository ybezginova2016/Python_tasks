# SGD на Python
# Напишите алгоритм SGD для модели линейной регрессии.
# Для этого объявим класс модели и создадим метод __init__ —
# инициализатор класса (англ. class initializer):
# англ. SGD для модели линейной регрессии
#
# class SGDLinearRegression:
#     def __init__(self):
#
# # Добавим в инициализатор класса один гиперпараметр — величину шага step_size:
# class SGDLinearRegression:
#     def __init__(self, step_size):
#
# # Теперь размер шага можно передать модели при создании класса:
# # размер шага выбрали произвольно
# model = SGDLinearRegression(0.01)
#
# # Сохраним размер шага в атрибуте:
# class SGDLinearRegression:
#     def __init__(self, step_size):
#         self.step_size = step_size

# 1. Разработку алгоритма SGD начните с заглушки. Загрузка данных
# и запуск алгоритмов уже в прекоде. Допишите класс модели:
# Добавьте в модель гиперпараметры epochs и batch_size. Соблюдая
# порядок, добавьте их в инициализатор класса и сохраните в
# атрибутах self.epochs и self.batch_size.

# В функции fit() задайте, что начальные веса w равны нулям.
# В функции predict() напишите формулу для вычисления предсказания.
# Функция print() выведет значения метрики R2 на экран.

# Вектор начальных весов создаётся так: np.zeros(X.shape[1]).

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

data_train = pd.read_csv('/datasets/train_data_n.csv')
features_train = data_train.drop(['target'], axis=1)
target_train = data_train['target']

data_test = pd.read_csv('/datasets/test_data_n.csv')
features_test = data_test.drop(['target'], axis=1)
target_test = data_test['target']


class SGDLinearRegression:
    def __init__(self, step_size, epoch, batch_size):
        self.step_size = step_size
        self.epochs = epoch
        self.batch_size = batch_size

    def fit(self, train_features, train_target):
        # Creating a matrix X - матрицу коэффициентов перед неизвестными
        X = np.concatenate((np.ones((train_features.shape[0], 1)), train_features), axis=1)
        y = train_target
        # Рассчитываем коэффициенты прямой по формуле.
        # w = np.linalg.inv(train_features.T @ train_features) @ train_features.T @ y
        # Вектор начальных весов создаётся так:
        w = np.zeros(X.shape[1])
        # в следующих задачах вы напишете здесь алгоритм SGD

        self.w = w[1:]
        self.w0 = w[0]

    def predict(self, test_features):
        return  test_features.dot(self.w) + self.w0


# мы уже передали подходящие для обучения параметры
model = SGDLinearRegression(0.01, 1, 200)
model.fit(features_train, target_train)

pred_train = model.predict(features_train)
pred_test = model.predict(features_test)

print(r2_score(target_train, pred_train).round(5))
print(r2_score(target_test, pred_test).round(5))