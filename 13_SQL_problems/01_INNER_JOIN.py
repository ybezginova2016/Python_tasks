# Задание
# Выведите все позиций списка товаров принадлежащие какой-либо
# категории с названиями товаров и названиями категорий. Список
# должен быть отсортирован по названию товара, названию категории.
# Для соединения таблиц необходимо использовать оператор INNER JOIN.
# Ожидаемый формат результата:
#
# +-------------+----------------+
# | good_name   | category_name  |
# +-------------+----------------+
# | good 1      | category 1     |
# | good 1      | category 2     |
# | good 2      | category 3     |
# | good 2      | category 4     |
# | good 3      | category 7     |
#
# Выборки, полученные с помощью оператора SELECT могут быть
# отсортированы по нескольким атрибутам. Для этого необходимо в
# операторе ORDER BY указать набор атрибутов через запятую в
# необходимом порядке.
# В запросе для соединения нескольких источников данных операцию
# соединения можно использовать многократно. Например, для соединения
# таблиц A, B и C.

SELECT good.name AS good_name, category.name AS category_name
FROM category_has_good
	INNER JOIN good ON category_has_good.good_id = good.id
	INNER JOIN category ON category_has_good.category_id = category.id
ORDER BY good.name, category.name;