#ГЕНЕРАТОР ЧИСЕЛ ФИБОНАЧЧИ
# v1.0 - буду пробовать оптимизировать

def fib(n=1):
    a = 0 
    i = 1
    yield i
    while n-1:
        if n % 2:
            i = a + i
            n -= 1
            yield i
        else: 
            a = a + i
            n -= 1
            yield a
        
        
n = int(input('Введите количество элементов последовательности Фибоначчи: '))
f = fib(n)

for i in f:
    print(i)