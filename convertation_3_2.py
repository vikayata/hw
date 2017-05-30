
# Создаем словарик для замены двухзначных чисел в шестнадцатиричной системе
# Если изменить механизм инициации словаря, данный модуль можно будет расширить,
# сделав универсальным - для любой системы счисления.

# Над вопросом, возможно, удобно ли и как использовать только один словарь, пока думаю.

let_dict = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}
let_dict2 = {
    '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'
}


# На вход всем функциям будет подаваться число в форме строки и основание системы счисления

# Реализация 1 - из десятичной в *

def convert_from_decimal(num, i):
    num = int(num)
    new_num = []                            # список остатков от деления
    while num >= i:                         # пока остаток больше базы
        part = int(num % i)                 # находим остаток
        #print(part, type(part))
        num = int((num - part) / i)         # реализация алгоритма - получение нового числа
        if part in let_dict2:             # проверка необходимости замены числа на букву - для системы с основанием > 10
            part = let_dict2.get(str(part))
        new_num.append(str(part))           # добавление в список остатков остатка в формате строки
        #print('num =', num)
    if num != 0:                            # если num меньше базы но больше нуля - добавляем в список остатков в формате строки
        new_num.append(str(num))
    #print(new_num)
    new_num = new_num[::-1]                 # инвертируем список остатков
    return int("".join(new_num))            # склеиваем список и возвращаем как число - вдруг работать с ним дальше нужно

#print(convert_from_decimal(22, 2))

# Реализация 2 - из * в десятичную

def convert_to_decimal(num, i):
    new_num = 0
    for j in range(len(num)):               # проходим по каждой позиции числа
        a = let_dict.get(num[-(j+1)]) if num[-(j+1)] in let_dict else num[-(j+1)] 
        # заменяем символ на число из словаря если символ - буква, или оставляем цифрой 
        new_num += (int(a) * (i ** j))      # суммируем начиная с единиц (конца строки) и нулевой степени
    return(new_num)
    
#print(convert_to_decimal(10110, 2))

def binary_to_decimal(a):
    return convert_to_decimal(a, 2)

def octal_to_decimal(a):
    return convert_to_decimal(a, 8)

def hex_to_decimal(a):
    return convert_to_decimal(a, 16)

def decimal_to_binary(a):
    return convert_from_decimal(a, 2)

def decimal_to_octal(a):
    return convert_from_decimal(a, 8)

def decimal_to_hex(a):
    return convert_from_decimal(a, 16)