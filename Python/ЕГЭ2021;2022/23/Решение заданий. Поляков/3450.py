'''
У исполнителя Калькулятор есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 5
3. Умножить на 3
Определите число, для получения которого из числа 1 существует 175 программ.
'''
# https://prnt.sc/YmKO8WSIfnpR


def func(start, end):
    if (end < start):
        return 0
    elif (end == start):
        return 1
    else:
        return func(start + 1, end) + func(start + 5, end) + func(start * 3, end)


for x in range(1, 1000):
    if func(1, x) == 175:
        print(x)
        break
