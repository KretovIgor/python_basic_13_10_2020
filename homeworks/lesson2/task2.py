list_1 = [input('Число 1: '), input('Число 2: '), input('Число 3: '), input('Число 4: '), input('Число 5: ')]
list_1[0], list_1[1] = list_1[1], list_1[0]
list_1[2], list_1[3] = list_1[3], list_1[2]
print(list_1)
