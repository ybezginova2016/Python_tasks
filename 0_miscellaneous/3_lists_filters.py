# Простой пример. Дан список raw_numbers с числами. Из них нужно отобрать только те, что больше 1000. Вот алгоритм такой программы:
# создаём пустой список для хранения результатов — filtered_numbers,
# цикл проходит по всем элементам списка raw_numbers,
# сравнивает элемент и 1000,
# если сравнение вернуло True — сохраняет элемент
# в filtered_numbers.


# исходный список
raw_numbers = [1, 10, 10000, -2, -0.5, 82, 3, 9999, 100]

# финальный список с подходящими числами
filtered_numbers = []

for number in raw_numbers:                # запускаем цикл
    if number > 1000:                     # проверяем условие для элемента списка
        filtered_numbers.append(number)   # сохраняем подходящий объект

print('Результат фильтрации:', filtered_numbers)

# Лаборатория фильтрации
# Из предыдущего урока вы узнали, что фильтрация объектов списка — это применение цикла for вместе с if. Цикл for проходит по всем объектам списка и применяет к ним различные действия в соответствии с прописанными в if условиями.

# Задача 1
# Список visitors_age хранит возраст посетителей на входе
# в парк экстремальных развлечений. Проследите, чтобы в парк
# попали только совершеннолетние. Cоздайте список entrance_allowed
# и добавьте в него все числа от 18 и больше
# из списка visitors_age.
visitors_age = [17, 10, 96, 30, 18, 82, 13, 84, 15, 41]

# создайте пустой список entrance_allowed
entrance_allowed = []

# пройдите циклом for по исходному списку
for age in visitors_age:
    if age >= 18:
        # проверьте, что число больше или равно 18
        entrance_allowed.append(age)
        # если это так – положите его в список entrance_allowed

print(entrance_allowed)

# Задача 2
# Посчитайте, сколько человек в итоге попадёт в парк.
# Это не совсем фильтр: создавать новый список с
# отфильтрованными элементами не придётся.
# Вместо этого — увеличивайте значение переменной
# counter на 1 каждый раз, когда выполняется условие.
# Без цикла и if здесь всё равно не обойтись.

visitors_age = [17, 10, 96, 30, 18, 82, 13, 84, 15, 41]

counter = 0

for age in visitors_age:
    if age >=18:
        counter +=1

print(counter)

# Задача 3
# Робот на складе крупного интернет-ритейлера собирает заказы.
# Помогите ему — добавьте в список order все элементы из списка
# storage, кроме подводной лодки.
storage = ['коробка печенья', 'подводная лодка', 'краски', 'горшок для цветка', 'отвёртка', 'музыкальная пластинка', 'блокнот']

order = []

for stor in storage:
    if stor != 'подводная лодка':
        order.append(stor)

print(order)

# Задача 4
# Список julia_songs хранит уникальные идентификаторы песен,
# которым Юля поставила лайк в музыкальном сервисе.
# Список mary_songs — песен, которые понравились Маше.
# Создайте плейлист, который понравится им обеим.
# Добавьте в список mary_julia_songs элементы,
# которые есть в обоих списках.

julia_songs = [145678, 297863, 966387, 374981, 746397, 197638]
mary_songs = [576093, 197638, 736901, 297863, 374981, 871532]

mary_julia_songs = []

for julia in julia_songs:
    for mary in mary_songs:
        if julia == mary:
            mary_julia_songs.append(julia)

print(mary_julia_songs)

# Задача 5
# В списке yellow_submarine_chorus некоторые значения повторяются.
# Создайте список yellow_submarine_briefly, в котором каждый
# элемент исходного списка встречается только раз.
yellow_submarine_chorus = ['we', 'all', 'live', 'in', 'a', 'yellow', 'submarine', 'yellow', 'submarine', 'yellow', 'submarine', 'we', 'all', 'live', 'in', 'a', 'yellow', 'submarine', 'yellow', 'submarine', 'yellow', 'submarine']

yellow_submarine_briefly = []

for chorus in yellow_submarine_chorus:
    if chorus not in yellow_submarine_briefly:
        yellow_submarine_briefly.append(chorus)

print(yellow_submarine_briefly)

# Задача 6
# Робот в службе поддержки повышает приоритет всех обращений,
# на которые не было ответа больше 10 часов. Количество часов,
# прошедших со времени поступления каждой заявки, лежит в списке
# hours_passed.
# Определите номера обращений, приоритет по которым следует
# повысить — если значение в hours_passed больше 10,
# сохраните его индекс в список high_priority
hours_passed = [9, 12, 8, 24, 35, 0, 15, 28]
high_priority = []

for hour in range(len(hours_passed)):
    if hours_passed[hour] >= 10:
        high_priority.append(hour)

print(high_priority)

for index in high_priority:
    print(hours_passed[index])

# Задача 7
# Два списка описывают объекты недвижимости:
# prices — стоимость аренды в долларах,
# addresses — адреса помещений.
# То есть аренда объекта по адресу addresses[index]
# стоит prices[index]. Составьте список адресов объектов,
# арендная ставка которых ниже 1000 долларов.

prices = [1100, 999, 1000000, 80, 40000]
addresses = ['Россия, Москва, Берсеневская набережная, 6с1',
             'Россия, Москва, Болотная набережная, 11с1',
             'Россия, Москва, Романов переулок, 4',
             'Россия, Москва, Старая Басманная улица, 20к1',
             'Россия, Москва, Волгоградский проспект, 32к8']

addresses_with_low_price = []

for price, address in zip(prices, addresses):
    if price <= 1000:
        addresses_with_low_price.append(address)
print(addresses_with_low_price)

#version 2
prices = [1100, 999, 1000000, 80, 40000]
addresses = ['Россия, Москва, Берсеневская набережная, 6с1',
             'Россия, Москва, Болотная набережная, 11с1',
             'Россия, Москва, Романов переулок, 4',
             'Россия, Москва, Старая Басманная улица, 20к1',
             'Россия, Москва, Волгоградский проспект, 32к8']

addresses_with_low_price = []

for i in range(len(prices)):
    if prices[i] <= 1000:
        addresses_with_low_price.append(addresses[i])

print(addresses_with_low_price)

#### Задача 8 ####
# Теперь объект недвижимости описывают уже четыре списка:
# prices — цена,
# floors — этаж,
# distances — расстояние до центра города в километрах,
# addresses — адрес.
# Создайте списки prices_filtered , floors_filtered,
# distances_filtered, addresses_filtered. С помощью
# фильтра найдите все объекты на первом этаже не дальше 15 км
# от центра города по ставке менее 1000 долларов. Объекты,
# которые находятся на расстоянии 15 км ровно,
# тоже нужно включить.
# Сохраните данные о таких объектах: цену — в prices_filtered,
# этаж — во floors_filtered, расстояние до центра —
# в distances_filtered, адрес — в addresses_filtered.

prices = [1100, 999, 80, 80, 40000]
floors = [10, 1, 1, 4, 30]
distances = [10, 3, 15, 31, 37]
addresses = ['Россия, Москва, Берсеневская набережная, 6с1',
					   'Россия, Москва, Болотная набережная, 11с1',
						 'Россия, Москва, Романов переулок, 4',
						 'Россия, Москва, Старая Басманная улица, 20к1',
						 'Россия, Москва, Волгоградский проспект, 32к8']

prices_filtered = []
floors_filtered = []
distances_filtered = []
addresses_filtered = []


for index in range(len(prices)):
    if (prices[index] < 1000 and
        floors[index] == 1 and
        distances[index] <= 15): # напишите составное условие
            prices_filtered.append(prices[index])
            floors_filtered.append(floors[index])
            distances_filtered.append(distances[index])
            addresses_filtered.append(addresses[index])

print(prices_filtered)
print(floors_filtered)
print(distances_filtered)
print(addresses_filtered)

# Это легко проверить. Составьте список из уникальных значений
# столбца area_unit и выведите этот список на экран.
import pandas
realty_df = pandas.read_csv('yandex_realty_data.csv')

unique_area_units = []

# найдите уникальные значения столбца 'area_unit'
# и поместите их в список unique_area_units
for uniq_unit in realty_df['area_unit']:
    if uniq_unit not in unique_area_units:
    # с помощью if проверьте, встречается ли это значение в unique_area_units
        unique_area_units.append(uniq_unit)

print(unique_area_units)

# Результат
# ['SQUARE_METER']

# Ровно таким же образом можно проверить столбец offer_type —
# тип предложения:
import pandas
realty_df = pandas.read_csv('yandex_realty_data.csv')

unique_offer_types = []

for offer_type in realty_df['offer_type']:
    if offer_type not in unique_offer_types:
        unique_offer_types.append(offer_type)

print(unique_offer_types)

# В датасете представлен только один вид предложений — RENT,
# то есть аренда. Значит, в исследовании эту колонку,
# как и area_unit, можно не учитывать.
# Теперь проверьте, какие бывают «типы аренды».
# Составьте список из уникальных значений столбца
# commercial_type и выведите этот список на экран.
import pandas
realty_df = pandas.read_csv('yandex_realty_data.csv')

unique_commercial_types = []

# найдите уникальные значения столбца 'commercial_type'
# и поместите их в список unique_commercial_types

for com_type in realty_df['commercial_type']:
    if com_type not in unique_commercial_types:
        unique_commercial_types.append(com_type)

print(unique_commercial_types)
# ['OFFICE', 'FREE_PURPOSE', 'RETAIL', 'WAREHOUSE']