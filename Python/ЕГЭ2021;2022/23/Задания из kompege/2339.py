'''
Исполнитель Калькулятор преобразует число, записанное на экране в троичной системе счисления. 
У исполнителя есть две команды, которым присвоены номера:

1. Умножь на 2
2. Умножь на 2 и прибавь 1

Сколько различных результатов можно получить из исходного числа 1 после выполнения программы, 
содержащей ровно 15 команд?
'''
# https://prnt.sc/tus6S7d16xfC



# (I) Решение

unique = set()


def func(start, count):
    if count == 15:
        unique.add(start)
        return True
    else:
        return func(start * 2, count + 1) + func(start * 2 + 1, count + 1)


func(1, 0)
print(len(unique))



# (II) Решение

arr = [1]


# "содержащей ровно 15 команд"
for _ in range(15): 
    for j in range(len(arr)):
        remaining = arr.pop(0)
        arr.append(2 * remaining)
        arr.append(remaining * 2 + 1)


print(len(arr))
