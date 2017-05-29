
# Aeyrwbb действий с ежедневником

def wait_for_instruction():
    j = int(input('Введите число:'))
    return j

def show_menu():
    print('1. Вывести список задач')
    print('2. Добавить задачу')
    print('3. Отредактировать задачу')
    print('4. Завершить задачу')
    print('5. Начать задачу сначала')
    print('6. Выход')
    
    return wait_for_instruction()


def show_tasks():
    print('Список задач')
    return 0

def add_task():
    print('Добавление задачи')
    return 0

def edit_task():
    print('Редактирование задачи')
    return 0

def end_task():
    print('Завершение задачи')
    return 0

def restart_task():
    print('Рестарт задачи')
    return 0

def exit_from_diary():
    return 6