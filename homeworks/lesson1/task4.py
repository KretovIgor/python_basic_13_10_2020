n = int(input('Ведите целое положительное число >>> \n'))
max_value = n % 10
while n > 0:
    variable_1 = n % 10
    n = n // 10
    if variable_1 > max_value:
        max_value = variable_1
print(f'Наибольшая цифра в числе {max_value}')