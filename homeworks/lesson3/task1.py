def division():
    try:
        num_1 = int(input('Введите число 1: '))
        num_2 = int(input('Введите число 2: '))
        result = int(num_1 / num_2)
        return result
    except ZeroDivisionError:
        return 'Деление на 0 невозможно'
    except ValueError:
        return 'Введено неверное значение'


print(division())
