#### EXERCISE 1 ####

# 1. Разбейте датасет о потреблении электроэнергии на обучающую и тестовую
# выборки в соотношении 4:1. Вам нужны данные за всё время. Из обучающей
# выборки удалите строки с пропусками.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
fig, ax = plt.subplots(figsize=(16, 11))

ax.plot(data['num_orders'])
ax.set_xlabel(data.count())
ax.set_ylabel('Number of Taxi Orders')

fig.autofmt_xdate()
plt.tight_layout())

def make_features(data, max_lag, rolling_mean_size):
    data['year'] = data.index.year
    data['month'] = data.index.month
    data['day'] = data.index.day
    data['dayofweek'] = data.index.dayofweek

    for lag in range(1, max_lag + 1):
        data['lag_{}'.format(lag)] = data['PJME_MW'].shift(lag)

    data['rolling_mean'] = data['PJME_MW'].shift().rolling(rolling_mean_size).mean()

# мы выбрали произвольные значения аргументов
make_features(data, 1, 1)

# WHY 'shuffle'?

# With time-series data, where you can expect auto-correlation in the data
# you should not split the data randomly to train and test set, but you
# should rather split it on time so you train on past values to predict
# future. Scikit-learn has the TimeSeriesSplit functionality for this.

# The shuffle parameter is needed to prevent non-random assignment to train
# and test set. With shuffle=True you split the data randomly.
# For example, say that you have balanced binary classification data and
# it is ordered by labels. If you split it in 80:20 proportions to train
# and test, your test data would contain only the labels from one class.
# Random shuffling prevents this.

train, test = train_test_split(data, shuffle=False, test_size=0.25)
train = train.dropna()

print(train.shape)
print(test.shape)

#### EXERCISE 2 ####

# 2. В выборке выделите признаки и целевой признак. На них обучите линейную
# регрессию и сохраните её в переменной model. Затем напечатайте на экране
# значения MAE для обучающей и тестовой выборок (уже в прекоде). Подберите
# аргументы функции make_features() так, чтобы значение MAE на тестовой
# выборке было не больше 37 000.

# MAE (Mean absolute error) represents the difference between the original
# and predicted values extracted by averaged the absolute difference over
# the data set. MSE (Mean Squared Error) represents the difference between
# the original and predicted values extracted by squared the average
# difference over the data set.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data.resample('1D').sum()


def make_features(data, max_lag, rolling_mean_size):
    data['year'] = data.index.year
    data['month'] = data.index.month
    data['day'] = data.index.day
    data['dayofweek'] = data.index.dayofweek

    for lag in range(1, max_lag + 1):
        data['lag_{}'.format(lag)] = data['PJME_MW'].shift(lag)

    data['rolling_mean'] = data['PJME_MW'].shift().rolling(rolling_mean_size).mean()


make_features(data, 6, 2)

train, test = train_test_split(data, shuffle=False, test_size=0.2)
train = train.dropna()

target_train = train['PJME_MW']
features_train = train.drop('PJME_MW', axis=1)

target_test = test['PJME_MW']
features_test = test.drop('PJME_MW', axis=1)

model = LinearRegression()
model.fit(features_train, target_train)

y_pred = model.predict(features_test)
y_pred_target = model.predict(features_train)

mae_train = mean_absolute_error(target_train, y_pred_target)
mae_test = mean_absolute_error(target_test, y_pred)

# MAE (Mean absolute error) represents the difference between the original and predicted values extracted by averaged the absolute difference over the data set. MSE (Mean Squared Error) represents the difference between the original and predicted values extracted by squared the average difference over the data set.

print("MAE обучающей выборки:", mae_train)
print("MAE тестовой выборки: ", mae_test)

# Output

# MAE обучающей выборки: 33615.82904024065
# MAE тестовой выборки:  36816.96596982049