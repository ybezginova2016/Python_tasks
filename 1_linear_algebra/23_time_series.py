import pandas as pd

data = pd.read_csv('/datasets/energy_consumption.csv')
print(data.info())

# 1. Измените тип данных Datetime с object на datetime64.
# Но прежде запустите код и просмотрите общую информацию о данных.
# В документации Pandas выберите любой способ преобразования данных.
# Формат вывода даты указывать не нужно: библиотека определит его
# самостоятельно.

# Преобразовать столбец можно двумя способами:
# передать в функцию read_csv() новый аргумент parse_dates (англ.
# «разобрать даты»),
# вызвать функцию pd.to_datetime().

import pandas as pd

# data = pd.read_csv('/datasets/energy_consumption.csv')

# OPTION 1 #
from datetime import datetime
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

data = pd.read_csv('/datasets/energy_consumption.csv', parse_dates=['Datetime'], date_parser=dateparse)
print(data.info())

# OPTION 2
data['Datetime'] = pd.to_datetime(data['Datetime'])
print(data.info())