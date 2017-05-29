from diary_functions import *
import datetime

diary_operations = (
    show_menu(), show_tasks(), add_task(), edit_task(), end_task(), restart_task(), exit_from_diary()  
)

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
    diary_operations[i]

