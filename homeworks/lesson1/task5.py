revenue = float (input('Сумма выручки >>> '))   #ВВод дохода
expense = float(input('Сумма издержек >>> '))   #Ввод расходов
if revenue > expense:
    print('Фирма работает с прибылью!')
    print('Рентабельность составляет', revenue/expense)
    stuff_number = int(input('Количество персонала фирмы >>> '))
    print('Прибыль фирмы в рассчете на одного сотрудника составляет', revenue/stuff_number)
else:
    print('Фирма работает в убыток')


