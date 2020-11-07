"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user(name: '',
         surname: '',
         birth_year: int,
         city: '',
         email: '',
         phone: ''):
    print(f'{surname} {name} родился в {birth_year} году, в городе {city}, эл.почта {email}, телефон {phone}')


get_name = input('Введите имя ')
get_surname = input('Введите фамилию ')
get_birth_year = int(input('Введите год рождения '))
get_city = input('Введите город проживания ')
get_email = input('Введите свой email ')
get_phone = int(input('Введите номер телефона (10 цифр) '))

user(name=get_name, surname=get_surname, birth_year=get_birth_year, city=get_city, email=get_email, phone=get_phone)