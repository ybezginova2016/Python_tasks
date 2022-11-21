# Качество прогноза

# Научимся измерять качество предсказания временных рядов и
# проверять модели на адекватность.
# Обучим модель с горизонтом прогнозирования в один день. Такие
# модели пригодятся в автоматизации принятия технических решений.
# Например, в задаче энергопотребления модель поможет изменять
# режим работы генераторов автоматически.
# Чтобы проверять качество моделей в наших задачах, возьмём метрику MAE.
# Её можно легко интерпретировать.

# Спрогнозировать временные ряды без обучения можно двумя способами:
# Все значения тестовой выборки предсказываются одним и тем же числом
# (константой). Для метрики MAE — это медиана.

# Новое значение x(t) прогнозируется предыдущим значением ряда,
# то есть x(t-1). Этот способ не зависит от метрики.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data.resample('1D').sum()

train, test = train_test_split(data, shuffle=False, test_size=0.2)

print("Средний объём электропотребления в день:", test['PJME_MW'].mean())

pred_median = np.ones(test.shape) * train['PJME_MW'].median()
mae = mean_absolute_error(pred_median, test['PJME_MW'])
print("MAE:", mae)

# Output
# Средний объём электропотребления в день: 745523.4529702971
# MAE: 96625.08333333333

# 745523 / 96625 ~ 13%, which is good.

#### 2 ####
# Для предсказания значений вызовите метод shift()
# у тестовой выборки. Чтобы заполнить первое значение,
# изучите, как работает атрибут iloc (от
# англ. integer location, «обращение
# по целочисленным индексам»).

# Используя train.iloc[-1] заменяем нулевой индекс в pred_previous
# минус первым трейновой выборки, это и будет предыдущее значение.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('/datasets/energy_consumption.csv', index_col=[0], parse_dates=[0])
data.sort_index(inplace=True)
data = data.resample('1D').sum()

train, test = train_test_split(data, shuffle=False, test_size=0.2)

print("Средний объём электропотребления в день:", test['PJME_MW'].mean())

pred_previous = test.shift(fill_value=train['PJME_MW'].iloc[-1])
mae = mean_absolute_error(pred_previous, test['PJME_MW'])
print("MAE:", mae)

# Output
# Средний объём электропотребления в день: 745523.4529702971
# MAE: 44941.65924092409



