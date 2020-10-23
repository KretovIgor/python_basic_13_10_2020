user_input = input('ВВедите предложение: ')
for el, word in enumerate(user_input.split(' ')):
    print(f'{el}:{word[:10]}')
