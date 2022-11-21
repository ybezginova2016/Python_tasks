# Разбейте датасет о потреблении электроэнергии на обучающую и
# тестовую выборки в соотношении 4:1. Возьмите данные за доступное время.
# Напечатайте на экране минимальные и максимальные значения индексов
# выборок (уже в прекоде). Они нужны, чтобы убедиться в корректности деления.

import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data.resample('1D').sum()

train, test = train_test_split(data, shuffle=False, test_size=0.2)

print(train.index.min(), train.index.max())
print(test.index.min(), test.index.max())

# output
# 2002-01-01 00:00:00 2015-04-09 00:00:00
# 2015-04-10 00:00:00 2018-08-03 00:00:00

# Обучающая выборка заканчивается 9 апреля 2015 года,
# а тестовая начинается 10 апреля 2015 года.