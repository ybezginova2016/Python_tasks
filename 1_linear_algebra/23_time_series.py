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

# OPTION 1 #
from datetime import datetime
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

data = pd.read_csv('/datasets/energy_consumption.csv', parse_dates=['Datetime'], date_parser=dateparse)
print(data.info())

# OPTION 2

data = pd.read_csv('/datasets/energy_consumption.csv')
data['Datetime'] = pd.to_datetime(data['Datetime'])
print(data.info())

# Output
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 145366 entries, 0 to 145365
# Data columns (total 2 columns):
#  #   Column    Non-Null Count   Dtype
# ---  ------    --------------   -----
#  0   Datetime  145366 non-null  datetime64[ns]
#  1   PJME_MW   145366 non-null  float64
# dtypes: datetime64[ns](1), float64(1)
# memory usage: 2.2 MB
# None

### 2. Установите индекс таблицы равным столбцу Datetime.
# В документации Pandas выберите любой способ установки индекса.
# Установить индекс таблицы можно двумя способами:
# функции read_csv() передать аргумент index_col (от англ. index
# column, «индексирующий столбец»)
import pandas as pd
data = pd.read_csv('/datasets/energy_consumption.csv', parse_dates=[0], index_col=0)
print(data.info())

# вызвать функцию df.set_index().
import pandas as pd
data = pd.read_csv('/datasets/energy_consumption.csv', parse_dates=[0])
data.set_index('Datetime', inplace = True)
print(data.info())

# Output
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 145366 entries, 2002-12-31 01:00:00 to 2018-01-02 00:00:00
# Data columns (total 1 columns):
#  #   Column   Non-Null Count   Dtype
# ---  ------   --------------   -----
#  0   PJME_MW  145366 non-null  float64
# dtypes: float64(1)
# memory usage: 2.2 MB
# None

### 3. Чтобы проверить, в хронологическом ли порядке расположены даты
# и время, посмотрите атрибут индекса таблицы is_monotonic (англ.
# «монотонный»). Если порядок соблюдён, атрибут вернёт True, если
# нет — False. Отсортируйте индекс таблицы. Метод найдите в
# документации. Напечатайте на экране значение атрибута is_monotonic.
# Затем вызовом функции info() выведите на экран общую информацию
# о таблице.

# Индекс сортируется методом sort_index()
# (англ. «отсортировать индекс»).

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.is_monotonic.html
import pandas as pd
data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])

data.sort_index(ascending=True, axis=0,
               level=None, inplace=True)
print(data.index.is_monotonic)
print(data.info())

# Output
# True
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 145366 entries, 2002-01-01 01:00:00 to 2018-08-03 00:00:00
# Data columns (total 1 columns):
#  #   Column   Non-Null Count   Dtype
# ---  ------   --------------   -----
#  0   PJME_MW  145366 non-null  float64
# dtypes: float64(1)
# memory usage: 2.2 MB
# None

### 4.Из временного ряда выделите данные с января по июнь 2018 года.
# Даты во временных рядах можно указывать в срезах. В прекоде выбраны
# значения с 2016 по 2017 год включительно.
import pandas as pd

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
# data = data['2016':'2017']
data = data['2018-01': '2018-06']
print(data.info())
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 4343 entries, 2018-01-01 00:00:00 to 2018-06-30 23:00:00
# Data columns (total 1 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   PJME_MW  4343 non-null   float64
# dtypes: float64(1)
# memory usage: 67.9 KB
# None

# 5. Постройте график временного ряда.
import pandas as pd

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data['2018-01':'2018-06']

# plotting
data['2018-01':'2018-06'].plot()
