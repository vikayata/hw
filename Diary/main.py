
from diary_functions import show_tasks as a
from diary_functions import add_task as b
from diary_functions import edit_task as c
from diary_functions import end_task as d
from diary_functions import restart_task as e
from diary_functions import exit_from_diary as f
from diary_functions import show_menu

diary_operations = [a, b, c, d, e, f]

# на данный момент рассматриваю, возможно ли организовывать функции списком без переменных-посредников

# diary_operations = [show_tasks(), add_task(), edit_task(), end_task(), restart_task(), exit_from_diary()]
# при инициализации словаря в данном случае функции срабатывают

'''tasks = (
    {
    'id': '',
    'name': '',
    'content': '',
    'deadline': ''
    }
)'''

i = 0
while i != 6:
    i = show_menu()
    diary_operations[i-1]()
    print()

