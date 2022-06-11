'''
У исполнителя Калькулятор есть три команды, которым присвоены номера:

1. Прибавить 1
2. Прибавить 5
3. Умножить на 3

Сколько разных чисел на отрезке [1000, 1024] может быть получено из числа 1 с помощью программ, 
состоящих из 8 команд?
'''
# https://prnt.sc/Ltse8bexInwl


unique = set()


def find_num(start, count):
    if count > 8:
        return None

    if (1000 <= start <= 1024) and (count == 8):
        unique.add(start)
    else:
        find_num(start + 1, count + 1)
        find_num(start + 5, count + 1)
        find_num(start * 3, count + 1)


find_num(1, 0)
print(len(unique))
