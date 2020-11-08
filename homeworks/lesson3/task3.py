"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""


def my_func(x, y, z):
    if x >= z and y >= z:
        return x + y
    elif x >= y and z >= y:
        return x + z
    elif y >= x and z >= x:
        return y + z


while True:
    try:
        var_1 = int(input('Введите число 1: '))
        var_2 = int(input('Введите число 2: '))
        var_3 = int(input('Введите число 3: '))
        print((my_func(var_1, var_2, var_3)))
        break
    except ValueError:
        print('Введите число!')
