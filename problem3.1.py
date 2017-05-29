import datetime as dt

def time_to_ny():
    today = dt.date.today()
    #print(type(today))

    new_year = dt.date(today.year, 12, 31)
    return abs(new_year - today).days

print('До Нового года осталось', time_to_ny(), 'дней.')