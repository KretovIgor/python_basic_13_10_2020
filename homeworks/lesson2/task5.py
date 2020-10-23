my_list = [7, 5, 3, 3, 2]
user_input = int(input('ВВедите новый элемент рейтинга (целое положительное число)(Для выхода нажмите "999") '))
while user_input != 999:
    for el in range(len(my_list)):
        if my_list[el] == user_input:
            my_list.insert(el + 1, user_input)
            break
        elif my_list[0] < user_input:
            my_list.insert(0, user_input)
        elif my_list[-1] > user_input:
            my_list.append(user_input)
        elif my_list[el] > user_input and my_list[el + 1] < user_input:
            my_list.insert(el + 1, user_input)
    print(f"текущий список - {my_list}")
    user_input = int(input("ВВедите новый элемент рейтинга (целое положительное число)(Для выхода нажмите '999') "))
