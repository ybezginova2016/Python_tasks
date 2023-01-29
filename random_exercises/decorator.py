"""
Напишите декоратор, который добавляет к списку аргументов строку — сказал он..
"""
def scream(func):
    def wrapper(*args):
        return func(*args, '— сказал он.')
    return wrapper

@scream
def say(*args):
    return ' '.join(args)

print(say('Нет,', 'я', 'твой', 'отец'))
# Нет, я твой отец — сказал он.