# Добавьте в столбец 'rolling_mean' скользящее среднее с размером окна,
# равным 10. Выведите на экран графики энергопотребления с января
# по июнь 2018 года и скользящего среднего

import pandas as pd

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data['2018-01':'2018-06'].resample('1D').sum()
data['rolling_mean'] = data.rolling(10).mean()
data.plot()