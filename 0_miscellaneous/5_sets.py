# Generating a set

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