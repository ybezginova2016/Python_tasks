# 1. Сложить все коробки в кучу.
# 2. Взять коробку и открыть.
# 3. Если внутри лежит коробка, добавить ее в кучу для последующего поиска.
# 4. Если внутри лежит ключ, поиск закончен!
# 5. Повторить.

# Рекурсивная функция для вычисления факториала

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))