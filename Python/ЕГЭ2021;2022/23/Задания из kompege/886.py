'''
Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, 
которым присвоены номера:

1. Прибавить 1
2. Прибавить 4
3. Умножить на 2

Сколько существует программ, состоящих из 7 команд, для которых при исходном 
числе 3 результатом является число 27?
'''
# https://prnt.sc/PU4cYMh-kNKx


def func(start, end, count):
    if (start > end):
        return 0
    elif (start == end) and (count == 7):
        return 1
    else:
        return func(start + 1, end, count + 1) + func(start + 4, end, count + 1) + func(start * 2, end, count + 1)


print(func(3, 27, 0))
