"""
Программа запрашивает у пользователя строку чисел,
разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом
и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких
 чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
  после этого завершить программу.
"""


def sum(numb_sum, input_string):
    input_list = input_string.split()
    for string_number in input_list:
        if string_number == "q":
            return numb_sum
        numb_sum += float(string_number)
    return numb_sum


summary = 0

while True:
    print(f"Сумма в настоящий момент {summary}")
    try:
        numbers = input("Введите числа через пробел или Q для выхода:  ".lower())
    except ValueError:
        print('Вводите числа!')
    summary = sum(summary, numbers)
    if "q" in numbers:
        print(f"Итоговое значение: {summary}")
        break
