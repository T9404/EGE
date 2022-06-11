'''
У исполнителя Калькулятор есть три команды, которым присвоены номера:

1. Прибавить 2
2. Прибавить 4
3. Прибавить 5

Определите число, для получения которого из числа 31 существует 1001 программа.
'''
# https://prnt.sc/fWvideRFeds4


def func(start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        return func(start + 2, end) + func(start + 4, end) + func(start + 5, end)


answer = [i for i in range(32, 60) if (func(31, i) == 1001)]
print(*answer)
