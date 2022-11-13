# ЗАДАНИЕ 10
# Выведите список товаров с названиями товаров и названиями
# категорий, в том числе товаров, не принадлежащих ни одной
# из категорий.


SELECT good.name, category.name FROM category_has_good
	LEFT OUTER JOIN category ON category_has_good.category_id = category.id
	RIGHT OUTER JOIN good ON category_has_good.good_id = good.id;

# ЗАДАНИЕ 11
# Выведите список товаров с названиями категорий, в том числе товаров,
# не принадлежащих ни к одной из категорий, в том числе категорий
# не содержащих ни одного товара.

SELECT good.name, category.name FROM category_has_good
	LEFT OUTER JOIN category ON category_has_good.category_id = category.id
	RIGHT OUTER JOIN good ON category_has_good.good_id = good.id
UNION
SELECT good.name, category.name FROM category_has_good
	RIGHT OUTER JOIN category ON category_has_good.category_id = category.id
	LEFT OUTER JOIN good ON category_has_good.good_id = good.id;

# ЗАДАНИЕ 12
# Выведите список всех источников клиентов и суммарный объем
# заказов по каждому источнику. Результат должен включать также
# записи для источников, по которым не было заказов.
SELECT source.name, sum(sale.sale_sum)
FROM source
	LEFT OUTER JOIN client
		ON source.id = client.source_id

	LEFT OUTER JOIN sale
		ON client.id = sale.client_id

GROUP BY source.name

;

# Для проверки существования записей в каких-либо таблицах можно использовать оператор EXISTS в условии WHERE. Например, вывести список категорий, к которым не принадлежат никакие товары можно следующим образом:
SELECT c.id, c.name FROM category AS c
  WHERE NOT EXISTS (SELECT * FROM category_has_good AS cg
        WHERE cg.category_id = c.id)
;

