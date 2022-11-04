# Generating a set
# В каких случаях использовать?
# Когда необходимо проверять принадлежит ли значение
# набору уникальных элементов и отсутствует необходимость
# поддерживать порядок в данном наборе.
"""
Верхняя граница n=100. Нужно сгенерировать множество чисел, которые
при делении на 5 дают в остатке 2 или 4,
при делении на 7 дают в остатке 3,
при делении на 3 НЕ дают в остатке 1.
"""
##### option 1 #####
n = 20
def set_gen(n):
    s = []
    for i in range(1, n+1):
        if i % 5 == 2 or i % 5 == 4:
            s.append(i)
        elif i % 7 == 3:
            s.append(i)
        elif i % 3 != 1:
            s.append(i)
    return s

print(set_gen(n))

##### option 2 #####

def new_set(n):
    D = set()
    for i in range(1, n+1):
        if i % 5 == 2 or i % 5 == 4:
            if i % 7 == 3:
                if i % 3 != 1:
                    D.add(i)
    return D

print(new_set(100))

set1 = set([1, 3, 5, 7, 9])
set2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

intersection = set1 & set2
print(intersection)

my_set = set()
my_set = {'hello world'}
print(my_set)

my_set = {s for s in range(10)}
print(my_set)

# множество удобно удаляет дубликаты
# dictionary oфициально упорядочены по времени добавления элементов
# индексация. Что списки, что кортежи — оба поддерживают
# индексацию и срезы, а вот множества — нет.
set_ex = set()
set_ex = {1, 1, 2, 3, 3, 4, 5, 5}
print(set_ex)