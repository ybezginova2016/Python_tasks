# В модуле tsa.seasonal (от англ. time series analysis, «анализ временных
# рядов») библиотеки statsmodels (англ. «статистические модели»)
# есть функция seasonal_decompose() (англ. «разбить на части»).
# Она раскладывает временной ряд на три составляющие: тренд,
# сезонность и остаток (англ. residuals). Это компонента, которая
# не объясняется трендом и сезонностью, это шум.

# from statsmodels.tsa.seasonal import seasonal_decompose
# decomposed = seasonal_decompose(data)

# Функция seasonal_decompose() принимает временной ряд,
# а возвращает объект структуры DecomposeResult (англ. «результат
# разделения»). В нём есть нужные атрибуты:

# decomposed.trend — тренд;
# decomposed.seasonal — сезонная составляющая;
# decomposed.resid — остаток декомпозиции.

# 1. Разложите временной ряд на тренд и сезонную компоненту.
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data['2018-01':'2018-06'].resample('1D').sum()

decomposed = seasonal_decompose(data)

plt.figure(figsize=(6, 8))
plt.subplot(311)
# Чтобы график корректно отобразился, указываем его
# оси ax, равными plt.gca() (англ. get current axis,
# получить текущие оси)
decomposed.trend.plot(ax=plt.gca())
plt.title('Trend')
plt.subplot(312)
decomposed.seasonal.plot(ax=plt.gca())
plt.title('Seasonality')
plt.subplot(313)
decomposed.resid.plot(ax=plt.gca())
plt.title('Residuals')
plt.tight_layout()
plt.show()

# 2. Постройте график сезонной составляющей за первые 15 дней
# января 2018 года. Сделайте срез компоненты decomposed.seasonal
# в промежутке от '2018-01-01' до '2018-01-15'. Затем вызовите
# функцию plot().

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)

decomposed = seasonal_decompose(data)
decomposed.seasonal['2018-01-01':'2018-01-15'].plot()