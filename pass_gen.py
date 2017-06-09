# ГЕНЕРАТОР ПАРОЛЕЙ

import random
import string

symbols = string.ascii_letters + string.digits + string.punctuation

def password_generator(n):
        while 1:
            password_parts = [random.choice(symbols) for x in range(n)]
            password = ''.join([str(i) for i in password_parts])
            yield password

n = int(input('Введите количество символов в пароле: '))
new_password = password_generator(n)

print('Сгенерирован пароль: {}'.format(next(new_password)))

