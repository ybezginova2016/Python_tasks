# 1. Календарные признаки (англ. calendar features)

data = pd.read_csv('energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data.resample('1D').sum()

# признак, в котором хранится год как число
data['year'] = data.index.year

# признак, в котором хранится день недели как число
data['dayofweek'] = data.index.dayofweek

print(data.head(10))

# 2. «Отстающие значения» (англ. lag features)

data['lag_1'] = data['PJME_MW'].shift(1)
data['lag_2'] = data['PJME_MW'].shift(2)
data['lag_3'] = data['PJME_MW'].shift(3)

print(data.head(10))

# 3. Скользящее среднее
data['rolling_mean'] = data['PJME_MW'].rolling(5).mean()
print(data.head(10))

# Скользящее среднее в моменте t учитывает текущее значение ряда x(t).
# Это некорректно: целевой признак «убежал» в признаки. Вычисление
# скользящего среднего не должно включать в себя текущее значение ряда.

#### EXERCISE 1 ####

# 1. Напишите функцию make_features() (англ. «создать признаки»),
# чтобы прибавить к таблице четыре новых календарных признака:
# год, месяц, день и день недели. Имена столбцов должны быть такие:
# 'year', 'month', 'day', 'dayofweek'. Примените функцию к таблице
# и напечатайте на экране её первые пять строк.

import pandas as pd

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data.resample('1D').sum()
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.month.html
def make_features(data):
    data['year'] = data.index.year
    data['month'] = data.index.month
    data['day'] = data.index.day
    data['dayofweek'] = data.index.dayofweek
    return data

make_features(data)
print(data.head())

#### EXERCISE 2 ####

# 2. Вычислите отстающие значения. В функцию make_features()
# добавьте новый аргумент max_lag, который задаст максимальный
# размер отставания. Новые признаки назовите: 'lag_1', 'lag_2' —
# и до величины max_lag. Примените функцию к таблице и напечатайте
# на экране её первые пять строк.

import pandas as pd
import numpy as np

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data.resample('1D').sum()

def make_features(data, max_lag):
    data['year'] = data.index.year
    data['month'] = data.index.month
    data['day'] = data.index.day
    data['dayofweek'] = data.index.dayofweek
# https://www.mikulskibartosz.name/forecasting-time-series-using-lag-features/
    for lag in range(1, max_lag + 1):
        data['lag_{}'.format(lag)] = data.PJME_MW.shift(lag)

make_features(data, 4)
print(data.head())

#### EXERCISE 3 ####

# 3. Вычислите скользящее среднее и добавьте его как признак 'rolling_mean'.
# В функцию make_features() добавьте новый аргумент rolling_mean_size,
# который задаст ширину окна. Текущее значение ряда для расчёта скользящего
# среднего применять нельзя.

import pandas as pd
import numpy as np

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


make_features(data, 4, 4)
print(data.head())




