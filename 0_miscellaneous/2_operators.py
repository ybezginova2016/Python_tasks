item = 'молоко'
shopping_list = ['хлеб', 'молоко', 'картофель', 'сыр', 'помидоры']

print(item in shopping_list)

print()

item = 'молоко'
shopping_list = ['хлеб', 'молоко', 'картофель', 'сыр', 'помидоры']

if item in shopping_list:
    print('Покупаем!')

    item = 'мармелад'
    shopping_list = ['хлеб', 'молоко', 'картофель', 'сыр', 'помидоры']

    if not item in shopping_list:
        print('Купим в другой раз!')


item = 'мармелад'
shopping_list = ['хлеб', 'молоко', 'картофель', 'сыр', 'помидоры']

if item not in shopping_list:
    print('Купим в другой раз!')

print('R' in 'Robot Robert')
print('Robert' in 'Robot Robert')
print('robot' in 'Robot Robert')

print("****************")
is_content = True

is_purring = is_content == True

print(is_purring)

print("****************")
is_content = False
clock = 10

is_purring = is_content == True or clock == 10

print (is_purring)

# Задача 3
# Мурчание — энергозатратный процесс.
# Запретите робокоту мурчать при заряде батареи меньше 10%. Состояние
# аккумулятора в процентах лежит в переменной battery.

is_content = True
clock = 10
battery = 9

is_purring = (is_content == True or clock == 10) and battery >= 10

print(is_purring)

# Переносы длинных условий
# Когда утверждение содержит больше двух-трёх частей,
# объединённых логическими операторами,
# читать его становится трудно:
if floor == 1 and price < 140000 and number_of_competitors <= 1 and distance_to_center < 30:
    print('Отличный вариант для аренды!')

# перенос
if (floor == 1 and
        price < 140000 and
        number_of_competitors <= 1 and
        distance_to_center < 30):
    print('Отличный вариант для аренды!')

client_message = 'Доброе утро'
print(client_message)

# добавьте к if новые варианты приветствия
if ('Здравствуйте'  in client_message or
    'Добрый день' in client_message or
    'Доброе утро' in client_message or
    'Привет' in client_message or
    'Добрый вечер' in client_message):
    print('Здравствуйте, с вами говорит искусственный интеллект: Агент Роберт I')
elif 'поломался' in client_message:
    print('Очень жаль! С ними такое обычно не случается. Попробуйте перезагрузить.')
else:
    print('Спасибо, что обратились! До свидания!')

print("**************")
client_message = 'Мой любимый робокот сломался!'
print(client_message)

if ('Здравствуйте' in client_message or
		'Добрый день' in client_message or
		'Доброе утро' in client_message or
		'Добрый вечер' in client_message or
    'Привет' in client_message):
    print('Здравствуйте, с вами говорит искусственный интеллект: Агент Роберт I')
# добавьте новые логические выражения через or в elif
elif ('поломался' in client_message or
        'не работает' in client_message or
      'кусается' in client_message or
      'завис' in client_message or
     'сломался' in client_message):
    print('Очень жаль! С ними такое обычно не случается. Попробуйте перезагрузить.')
else:
    print('Спасибо, что обратились! До свидания!')

print("****************")
client_message = 'Как включить функцию тихого мурчания? Робокот отличный, но будит по ночам.'
print(client_message)

if ('Здравствуйте' in client_message or
		'Добрый день' in client_message or
		'Доброе утро' in client_message or
		'Добрый вечер' in client_message or
    'Привет' in client_message):
    print('Здравствуйте, с вами говорит искусственный интеллект: Агент Роберт I')
elif ('поломался' in client_message or
      'сломался' in client_message or
      'не работает' in client_message or
      'кусается' in client_message or
      'завис' in client_message):
    print('Очень жаль! С ними такое обычно не случается. Попробуйте перезагрузить.')
elif ('телефон' in client_message or
      'звонить' in client_message):
    print('Наш телефон: 8 (800) 111-11-11')
elif ('время работы' in client_message or
      'открыты' in client_message):
    print('С 9 утра до 20 вечера в любой день недели')
# новое условие с elif — на случай прощания
elif ('о свидания' in client_message or
    'пасибо' in client_message): # исправьте код здесь
    print('Спасибо, что обратились! До свидания!')
else:
    print('Не могу помочь... Передам ваш вопрос специалисту.')