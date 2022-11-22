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