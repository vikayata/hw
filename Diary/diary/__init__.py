
import sys

from diary import storage

get_connection = lambda: storage.connect('diary.sqlite')


def wait_for_instruction():
    j = input('\nВведите команду: ')
    
    return j


def show_menu(): # отступы в меню намеренные, так читабельнее в консоли
    print(''' 
    ЕЖЕДНЕВНИК v1.0

    1. Вывести список задач
    2. Добавить задачу
    3. Отредактировать задачу
    4. Завершить задачу
    5. Начать задачу сначала
    6. Выход''')
    
    return wait_for_instruction()


def show_tasks():
    day = input('Введите день: ')
    print('\n     СПИСОК ЗАДАЧ')
    with get_connection() as conn:
        tasks = storage.find_task_by_dealine(conn, day)

        for task in tasks:
            print('{task[id]} - {task[name]} - {task[task]} - {task[deadline]}'.format(task=task))

    input('\nДля продолжения работы нажмите Enter')
    return '0'

def add_task():
    print('\n     ДОБАВЛЕНИЕ ЗАДАЧИ')
    name = input('\nВведите название задачи: ')
    task = input('Введите содержание задачи: ')
    try:    
        deadline = input('Введите срок выполнения задачи: ')
        
        with get_conneсtion() as conn:
            storage.add_task(conn, name, task, deadline)

        print('Новая задача создана.')
    except:
        print('Неправильно введена дата.')

    input('\nДля продолжения работы нажмите Enter')
    return '0'

def edit_task():
    print('\n     РЕДАКТИРОВАНИЕ ЗАДАЧИ')
    
    id = input('\nВведите номер задачи, которую вы хотите отредактировать: ')

    if id:
        with get_connection() as conn:
            task_to_change = storage.find_task_by_id(conn, id)

        if task_to_change:
            choice_dict = {'n': taskname, 't': task}
            choice = input('\nДля редактирования имени задачи введите\'n\', для редактирования содержания задачи введите\'t\'')
            while not choice_dict.get(choice):
                choice = input('\nВведите другую команду')

            change = input('\nВведите новое значение: ')
            storage.edit_task(conn, id, choice_dict.get(choice), change)
            print('Задача {} отредактирована.'.format(id))
        else:
            print('Задача не найдена.')

    input('\nДля продолжения работы нажмите Enter')
    return '0'

def end_task():
    print('\n     ЗАВЕРШЕНИЕ ЗАДАЧИ')

    id = input('\nВведите номер задачи, которую вы хотите завершить: ')

    if id:
        with get_connection() as conn:
            task_to_change = storage.find_task_by_id(conn, id)

        if task_to_change:
            storage.end_task(conn, id)
        else:
            print('Задача не найдена.')

    input('\nДля продолжения работы нажмите Enter')
    return '0'

def restart_task():
    print('\n     РЕСТАРТ ЗАДАЧИ')

    id = input('\nВведите номер задачи, которую вы хотите начать заново: ')

    if id:
        with get_connection() as conn:
            task_to_change = storage.find_task_by_id(conn, id)

        if task_to_change:
            try:
                new_deadline = input('\nВведите новый срок выполнения задачи: ')
                storage.restart_task(conn, id, new_deadline)
            except:
                print('Неправильно введена дата.')
        else:
            print('Задача не найдена.')

    input('\nДля продолжения работы нажмите Enter')
    return '0'

def exit_from_diary():
    sys.exit(0)

def main():
    with get_connection() as conn:
        storage.initialize(conn)

    diary_operations = {
        '0': show_menu, 
        '1': show_tasks, 
        '2': add_task, 
        '3': edit_task, 
        '4': end_task, 
        '5': restart_task, 
        '6': exit_from_diary
    }        
    
    i = '0'
    while i:
        cmd = diary_operations.get(i)

        if cmd:
            i = cmd()
        else:
            print('Неизвестная команда!')
            i = wait_for_instruction()

        