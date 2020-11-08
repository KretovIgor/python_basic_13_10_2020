"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user():
    global name, surname, birth_year, city, email, phone
    user_data = f'{surname} {name} родился в {birth_year} году, в городе {city}, эл.почта {email}, телефон {phone}'
    return user_data


try:
    name = input('Введите имя ')
    surname = input('Введите фамилию ')
    birth_year = int(input('Введите год рождения '))
    city = input('Введите город проживания ')
    email = input('Введите свой email ')
    phone = int(input('Введите номер телефона (10 цифр) '))
except (NameError, ValueError):
    print('Введено неверное значение')

print(user())

# print(f'{surname} {name} родился в {birth_year} году, в городе {city}, эл.почта {email}, телефон {phone}')


# user(name=get_name, surname=get_surname, birth_year=get_birth_year, city=get_city, email=get_email, phone=get_phone)
