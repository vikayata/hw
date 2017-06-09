# ДЕКОРАТОР ПРИОСТАНОВКИ ФУНКЦИИ

import time
   
def pause(n):
    
    def timer(n):
        while n:
            print('{} сек'.format(n))
            time.sleep(1)
            n -= 1

    def decorator(func):
        def wrapper(*args, **kwargs):
            print('Запрос на выполнение функции {} принят. Функция будет выполнена через: '.format(func.__name__))
            timer(n)
                        
            return func(*args, **kwargs)

        return wrapper

    return decorator

@pause(15)
def random_func():
    print('Hello world!')

random_func()