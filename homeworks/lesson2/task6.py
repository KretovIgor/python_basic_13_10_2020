# numeric = 0
# articles = []
# while input('Хотите добавить товар? Да/Нет ').lower() == 'да':
#    numeric += 1
#    features = {}
#    feature_key = str(input('Введите название товара: '))
#    feature_value = float(input('Цена товара: '))
#    feature_number = int(input('Количество: '))
#    features[feature_key] = feature_value, feature_number
#    articles.append([numeric, features])
#    print(articles)
# if input() == 'нет'.lower():
#    print('До свидания ')
# else:
#    print('Введен неверный ответ.')

goods = []
features = {'название': '', 'цена': '', 'количество': ''}
analytics = {'название': [], 'цена': [], 'количество': []}
numeric = 0
while True:
    control = input("Для выхода нажмите 'Q', для продолжения нажмите 'Enter', для аналитики нажмите 'A' ").lower()
    if control == 'Q'.lower():
        print('До свидания')
        break
    numeric += 1
    if control == 'A'.lower():
        print(f'Аналитика \n {"-"}')
        for key, value in analytics.items():
            print(f'{key}, {value}')
            print("-")
    for f in features.keys():
        feature_ = input(f'Введите "{f}" товара ')
        features[f] = feature_ if (f == 'название' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((numeric, features))
