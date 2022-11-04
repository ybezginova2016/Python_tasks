def secret_function(num):
    return num**2

number_list = [2, 3, 4, 5]

# возвращает адрес  объекта
# объект map является итератором наших результатов
print(map(secret_function, number_list))

# более удобная форма вывода
print(list(map(secret_function, number_list)))

print(list(zip([1, 2, 3], ['apple', 'grape', 'orange'], ['x', 'y', 'z'])))

# фунция map служит для модификации обьектов
# вот код который делает тоже самое что и map(secret_function, number_list)

def my_func(my_list):
    res_list = []
    for item in my_list:
        res_list.append(secret_function(item))
    return res_list
# map используется когда тебе надо пройтись по листу и что-то сделать с элементами внутри листа