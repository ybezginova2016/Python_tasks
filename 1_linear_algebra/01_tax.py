### TASK ###

### Вычисляем налог и сумму чаевых в ресторане
tax_rate = 0.05
tip_rate = 0.18

# В моем регионе налог составляет 5 %.
# В языке Python 5 % и 18 % представляются как
# 0.05 и 0.18 соответственно.

# Запрашиваем сумму счета у пользователя
cost = float(input("Введите сумму счета: "))

# Вычисляем сумму налога и чаевых
tax = cost * tax_rate
tip = cost * tip_rate
total = cost + tax + tip

# Отобразим результат
print("Налог составил f%, чаевые – f%, общая сумма", \
      "заказа: f%", "\n", (tax, tip, total))

# Знак обратной косой черты (\) называется символом продолжения строки. Он со-
# общает Python о том, что инструкция будет продолжена на следующей строке. Не
# вводите пробелы и иные символы, включая символ табуляции, после косой черты.