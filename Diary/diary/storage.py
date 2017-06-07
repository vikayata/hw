import sqlite3
import os.path as Path

# Переменные, содержащие строки sql-запросов

SQL_SELECT_ALL = '''
    SELECT id, taskname, task, deadline, status
    FROM 
        diary
'''

SQL_SELECT_TASKNAME_BY_ID = SQL_SELECT_ALL + ' WHERE id=?'

SQL_SELECT_TASKNAME_BY_DEADLINE = SQL_SELECT_ALL + ' WHERE deadline=?'

SQL_INSERT_TASK = '''
    INSERT INTO diary (taskname, task, deadline)
    VALUES (?, ?, ?)
'''

SQL_UPDATE_TASK = '''
    UPDATE diary SET ?=? WHERE id=?
'''

SQL_UPDATE_STATUS = '''
    UPDATE diary SET deadline=?, status=? WHERE id=?
'''

# Функция принимает курсор и исходную строку как кортеж 
# и возвращает реальную строку результата.
# >> реализуем возврат объекта, который может
# получать доступ к столбцам по имени.
def dict_factory(cursor, row):
    d = {}
    
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Функция (создает и) возвращает объект-соединение БД (~ образ).
def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn


# Функция, создающая БД
def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'db_structure.sql')
        with open(script_file_path) as f:
            conn.executescript(f.read())


def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def find_task_by_id(conn, id):
    with conn:
        cursor = conn.execute(SQL_SELECT_TASKNAME_BY_ID, (id,))
        return cursor.fetchone()


def find_task_by_deadline(conn, deadline):
    with conn:
        cursor = conn.execute(SQL_SELECT_TASKNAME_BY_DEADLINE, (deadline,))
        return cursor.fetchall()


def add_task(conn, taskname, task, deadline):
    # Ошибка?
    with conn:
        cursor = conn.execute(SQL_INSERT_TASK, (taskname, task, deadline))
        return 1 # вернем единичку как успех


def edit_task(conn, id, col, change):
    with conn:
        cursor = conn.execute(SQL_UPDATE_TASK, (col, change, id))
        return 1


def end_task(conn, id):
    with conn:
        cursor = conn.execute(SQL_UPDATE_STATUS, (0, id))
        return 1


def restart_task(conn, id, deadline):
    with conn:
        cursor = conn.execute(SQL_UPDATE_STATUS, (deadline, 1, id))
        return 1