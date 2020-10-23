"""
some comment
multi
string
"""

# todo Объяснить типы
# обычный коммент
#some_variable: int = 1  #int
#home_number = 22

#mass: float = 22.345  #float
#street_name = 'Ленина'  #string

#mass2 = 344.55

#mass3: float = mass + mass2
#mass4: float = some_variable + mass2

this_year = 2020
#name = input('Ваше имя \n>>>')
#surname = input('Ваша фамилия\n>>>')
age = int(input('Ваш возраст\n>>>'))


#full_user_data = f'Пользователь {name:>20}  {surname:<20} {this_year-int(age)} года рождения'

#print(full_user_data)

b_one = True
b_two = False

if int(age) >= 18:
    print('Доступ везду включая ХХХ')
    if int(age) > 30:
        print('Пока все дома')
elif age >= 16:
    print('Доступ к контенту 16+')
elif age<12:
    print('смотри только мультики')
else:
    print('Доступ к системе закрыт')



