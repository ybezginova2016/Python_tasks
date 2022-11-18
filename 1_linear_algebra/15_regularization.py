# Чем меньше значения весов, тем проще обучается алгоритм.
# Чтобы понять, насколько веса велики, вычисляют расстояние от вектора
# весов до вектора, состоящего из нулей. Например, квадрат евклидова
# расстояния d₂(w, 0) равен скалярному произведению весов на себя:
# (w, w).

# Если для регуляризации весов применяется евклидово расстояние,
# то такая линейная регрессия называется гребневой регрессией
# (англ. ridge regression).

##### EXERCISE 1 #####

# Добавьте в модель регуляризацию.
# Допишите код регуляризации:
# приравняйте элемент с индексом ноль в векторе reg к нулю
# (обычно сдвиг не включается в регуляризацию);
# к градиенту функции прибавьте слагаемое для регуляризации.

# В код модели из прошлой задачи мы добавили:
# новый гиперпараметр — вес регуляризации (reg_weight);
# обучение и тестирование с разными значениями.

# Слагаемое для регуляризации равно self.reg_weight * reg.

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
    def __init__(self, step_size, epochs, batch_size, reg_weight):
        self.step_size = step_size
        self.epochs = epochs
        self.batch_size = batch_size
        self.reg_weight = reg_weight

    def fit(self, train_features, train_target):
        X = np.concatenate((np.ones((train_features.shape[0], 1)), train_features), axis=1)
        y = train_target
        w = np.zeros(X.shape[1])

        for _ in range(self.epochs):
            batches_count = X.shape[0] // self.batch_size
            for i in range(batches_count):
                begin = i * self.batch_size
                end = (i + 1) * self.batch_size
                X_batch = X[begin:end, :]
                y_batch = y[begin:end]

                gradient = 2 * X_batch.T.dot(X_batch.dot(w) - y_batch) / X_batch.shape[0]
                # копируем вектор w, чтобы его не менять
                reg = 2 * w.copy()
                reg[0] = 0
                gradient += self.reg_weight * reg

                w -= self.step_size * gradient

        self.w = w[1:]
        self.w0 = w[0]

    def predict(self, test_features):
        return test_features.dot(self.w) + self.w0


# Чтобы сравнить гребневую регрессию с линейной, начнём с
# веса регуляризации, равного 0. Затем добавим
# обучение с его различными значениями.
print("Регуляризация:", 0.0)
model = SGDLinearRegression(0.01, 10, 100, 0.0)
model.fit(features_train, target_train)
pred_train = model.predict(features_train)
pred_test = model.predict(features_test)
print(r2_score(target_train, pred_train).round(5))
print(r2_score(target_test, pred_test).round(5))

print("Регуляризация:", 0.1)
model = SGDLinearRegression(0.01, 10, 100, 0.1)
model.fit(features_train, target_train)
pred_train = model.predict(features_train)
pred_test = model.predict(features_test)
print(r2_score(target_train, pred_train).round(5))
print(r2_score(target_test, pred_test).round(5))

print("Регуляризация:", 1.0)
model = SGDLinearRegression(0.01, 10, 100, 1.0)
model.fit(features_train, target_train)
pred_train = model.predict(features_train)
pred_test = model.predict(features_test)
print(r2_score(target_train, pred_train).round(5))
print(r2_score(target_test, pred_test).round(5))

print("Регуляризация:", 10.0)
model = SGDLinearRegression(0.01, 10, 100, 10.0)
model.fit(features_train, target_train)
pred_train = model.predict(features_train)
pred_test = model.predict(features_test)
print(r2_score(target_train, pred_train).round(5))
print(r2_score(target_test, pred_test).round(5))

# Output #
# Регуляризация: 0.0
# 0.21882
# 0.06296
# Регуляризация: 0.1
# 0.21488
# 0.07001
# Регуляризация: 1.0
# 0.16661
# 0.08061
# Регуляризация: 10.0
# 0.03945
# 0.02412

# Слишком слабая регуляризация R2 не меняется&