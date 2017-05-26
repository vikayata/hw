import datetime as dt

today = dt.date.today()
#print(type(today))

new_year = dt.date(today.year, 12, 31)
time_to_new_year = abs(new_year - today)
print('До Нового года осталось', time_to_new_year.days, 'дней.')