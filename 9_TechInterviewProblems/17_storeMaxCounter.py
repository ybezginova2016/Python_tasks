# Алгоритм работы:

# 1) посчитать количество повторяющихся элементов в листе
# 2) найти максимальное количество повторяющихся элементов
# 3) из словаря найти ключи которые по значению совпадают с максимальным
# значением и добавить в новый лист
# 4) отсортировать новый лист в алфавитном порядке и взять последний элемент

products = ['redShirt', 'redShirt', 'greenPans', 'blackPans', 'orangeShoes', 'blackPans']

def futuresProduct(products: list[str]):
    purchase_count_dict = {} # (key, value)
    for item in products:
        if item in purchase_count_dict.keys():
            purchase_count_dict[item] += 1
        else:
            purchase_count_dict[item] = 1

    # {'redShirt': 2, 'greenPans': 1, 'blackPans': 2, 'orangeShoes': 1}
    max_purchase = max(purchase_count_dict.values()) # в values лежат все значения ключей словаря
    list_purchase = []
    for product, counter in purchase_count_dict.items(): # в items лежит пара (key, value)
        if max_purchase == counter:
            list_purchase.append(product)
    sorted_purchase = sorted(list_purchase)
    return sorted_purchase[-1]

print(futuresProduct(products))

