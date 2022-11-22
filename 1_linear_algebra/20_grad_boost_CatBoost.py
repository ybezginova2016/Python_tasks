import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('travel_insurance.csv')
print(data.head())

features_train, features_valid, target_train, target_valid = train_test_split(
    data.drop('Claim', axis=1), data.Claim, test_size=0.25, random_state=12345)

# В категориальных признаках есть пропуски, записанные как новые
# значения: например, None в столбце Gender. Для CatBoost это не
# проблема, для библиотеки они — это отдельная категория.

# Импортируем из библиотеки CatBoostClassifier (англ. «классификатор
# CatBoost») и создадим модель. Поскольку у нас задача классификации,
# укажем логистическую функцию потерь. Итераций будет 10, чтобы не
# ждать долго.

from catboost import CatBoostClassifier

model = CatBoostClassifier(loss_function="Logloss", iterations=10)

# Обучим модель методом fit(). Помимо целевого признака и признаков,
# передадим модели категориальные признаки:

cat_features = ['Agency', 'Agency Type', 'Distribution Channel',
                'Product Name', 'Destination', 'Gender']

model.fit(features_train, target_train, cat_features=cat_features)

# Когда итераций много и на каждой информация выводиться не должна,
# применяют аргумент verbose (англ. «подробный»):

model = CatBoostClassifier(loss_function="Logloss", iterations=50)
model.fit(features_train, target_train, cat_features=cat_features, verbose=10)

# Предсказание вычисляется методом predict():
pred_valid = model.predict(features_valid)
# Вы уже знакомы с некоторыми параметрами, которые могут сильно
# повлиять на результат обучения. Это максимальная глубина дерева
# depth, скорость обучения learning_rate и количество деревьев в
# ансамбле iterations.

##### EXERCISE #####

# Подберите такие гиперпараметры модели, чтобы получить значение
# AUC-ROC не меньше 0.822 — наилучшего результата этой метрики
# из курса «Обучение с учителем». Можете попробовать получить
# и больше. Напечатайте на экране значение метрики AUC-ROC.

# Значение iterations следует подобрать так, чтобы и метрика
# получилась больше 0.822, и считалось быстро. Подойдёт 150 итераций,
# но это не идеал. Остальные гиперпараметры не меняйте.
import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.metrics import roc_auc_score

data = pd.read_csv('/datasets/travel_insurance.csv')

features_train, features_valid, target_train, target_valid = train_test_split(
    data.drop('Claim', axis=1), data.Claim, test_size=0.25, random_state=12345)

cat_features = ['Agency', 'Agency Type', 'Distribution Channel',
                'Product Name', 'Destination', 'Gender']

model = CatBoostClassifier(loss_function="Logloss", iterations=150)

model.fit(features_train, target_train, cat_features=cat_features, verbose=10)

probabilities_valid = model.predict_proba(features_valid)
probabilities_one_valid = probabilities_valid[:, 1]
print(roc_auc_score(target_valid, probabilities_one_valid))

# Output: 0.8247308961352839

# Улучшить метрику для CatBoost легче простого. Если продолжить настройку гиперпараметоров,
# то можно довести до идеальной.
