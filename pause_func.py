# ДЕКОРАТОР ПРИОСТАНОВКИ ФУНКЦИИ

import time

def pause(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('''
Запрос на выполнение функции {} принят. Функция будет выполнена через {} секунд. 
'''.format(func.__name__, n))
            time.sleep(n)
            return func(*args, **kwargs)

        return wrapper

    return decorator

@pause(10)
def random_func():
    print('Hello world!')

random_func()
