# O(1)

book = dict()

book['apple'] = 0.67
book['milk'] = 1.48
book['avocado'] = 1.48

print(book)

# Запросим цена авокадо
print(book['avocado'])

# Хеш-таблица состоит из ключей и значений.
# В хеше book имена продуктов являются ключами,
# а цены - значениями. Хеш-таблица связывает
# ключи со значениями.

# создадим хеш для хранения информации об уже проголосовавших людях
voted = {}

def check_voter(name):
    if voted.get(name):
        print('Kick them out!')
    else:
        voted[name] = True
        print('Let them vote!')

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data