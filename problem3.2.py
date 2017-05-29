from convertation_3_2 import *

# Проверяем работоспособность модуля
# Простым методом, не будем делать интерфейс ввода

number = input('Введите число x в десятичной системе:')
print(number, type(number))

print(
    'x в двоичной системе:', decimal_to_binary(number),
    'x в восьмеричной системе:', decimal_to_octal(number),
    'x в шестнадцатиричной системе:', decimal_to_hex(number),
)

number = input('Введите число x в двоичной системе:')
print('x в десятичной системе:', binary_to_decimal(number))

number = input('Введите число x в двоичной системе:')
print('x в десятичной системе:', octal_to_decimal(number))

number = input('Введите число x в двоичной системе:')
print('x в десятичной системе:', hex_to_decimal(number))