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
import numpy as np

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

