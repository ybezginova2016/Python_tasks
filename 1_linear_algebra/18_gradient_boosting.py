# Gradient Boosting

# Если объединить бустинг и градиентный спуск, получим градиентный бустинг!
# Каждая базовая модель в бустинге старается «сдвинуть» предсказания
# прошлого шага в сторону правильных ответов. Так минимизируют
# функцию потерь. Градиентный спуск помогает делать это эффективнее.

# Мы по-прежнему будем минимизировать функцию потерь. Но аргументом,
# по которому идёт спуск, станут ответы модели!
# Это и есть градиентный бустинг (англ. gradient boosting).

# Описание бустинга, есть описание гиперпараметров - https://alexanderdyakonov.files.wordpress.com/2017/06/book_boosting_pdf.pdf
# примеры использоваиня xgboost,lightgbm, catboost - https://github.com/V-Marco/MO_dvfu_2022/blob/main/seminar_9/sem09_boostings_part2.ipynb
# про гиперпараметр гамма и его тюнинг - https://medium.com/data-design/xgboost-hi-im-gamma-what-can-i-do-for-you-and-the-tuning-of-regularization-a42ea17e6ab6
# гиперпараметры в lightgbm (+как тюнить) - https://neptune.ai/blog/lightgbm-parameters-guide
# Для подбора гиперпараметров можно использовать две либы - bayes_opt и scikit-optimize
# Пример bayes_opt на lightgbm - https://www.kaggle.com/code/rsmits/bayesian-optimization-for-lightgbm-parameters/notebook
# Документация по scikit-optimize - https://scikit-optimize.github.io/stable/

# И чуток про стэкинг
# Что такое и как, зачем использовать - https://alexanderdyakonov.wordpress.com/2017/03/10/c%D1%82%D0%B5%D0%BA%D0%B8%D0%BD%D0%B3-sta[…]1%D0%BB%D0%B5%D0%BD%D0%B4%D0%B8%D0%BD%D0%B3-blending/
# Пример самописного стэкинга - https://github.com/Dyakonov/ml_hacks/blob/master/dj_stacking.ipynb
# Документация стэкинга в sklearn - https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html