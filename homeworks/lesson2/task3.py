seasons = {'Winter': (12, 1, 2),
           'Spring': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}
month = int(input('Введите месяц от 1 до 12: '))

for item in seasons.keys():
    if month in seasons[item]:
       print(item)
