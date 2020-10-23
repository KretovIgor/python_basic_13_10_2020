time_sec_user = int(input('Введите количество секунд>>> \n'))
time_hour = int(time_sec_user / 3600)
time_min = int((time_sec_user - time_hour * 3600) / 60)
time_sec = int(time_sec_user - time_hour * 3600 - time_min * 60)
time_hms = f'{time_hour} часа(ов) {time_min} минут {time_sec} секунд'
print(time_hms)

