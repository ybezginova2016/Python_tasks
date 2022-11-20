# Чтобы поменять интервал и сгруппировать значения, вызовем функцию
# resample(). В аргументе укажем новый интервал. Например:

# 1H англ. hour, 1 час
data.resample('1H')

# 2W англ. week, 2 недели
data.resample('2W')

# 1. Постройте график среднего потребления электроэнергии по годам.
import pandas as pd

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data.resample('1Y').mean()
data.plot()

# 2. Постройте график энергопотребления с января по июнь 2018 года.
# Выберите интервал в один день, по каждому — вычислите суммарное
# энергопотребление.
import pandas as pd

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)

data['2018-01':'2018-06'].resample('1D').sum().plot()