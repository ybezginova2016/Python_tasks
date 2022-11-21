# Вычислите разности временного ряда. Пропущенные значения
# заполнять не нужно. На графике изобразите скользящее среднее
# и скользящее стандартное отклонение.

# Из данных за январь-июнь 2018 нужно вычесть результат вызова
# метода shift().
import pandas as pd

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data['2018-01':'2018-06'].resample('1D').sum()
data = data['2018-01':'2018-06'] - data.shift()
data['mean'] = data['PJME_MW'].rolling(15).mean()
data['std'] = data['PJME_MW'].rolling(15).std()
data.plot()
# Ряд стал более стационарным, а значит, данные можно прогнозировать.

