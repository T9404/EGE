'''
Откройте файл электронной таблицы 9-130.xls, содержащей в каждой строке 
три натуральных числа. Выясните, какое количество троек могут перестановкой 
образовать арифметическую прогрессию с не нулевой разностью прогрессии.
'''
# https://prnt.sc/qtTOzqgmqxQF


from itertools import permutations


f = open('9-130.csv')


count = 0


for _ in range(5000):
    a, b, c = map(int, f.readline().split(','))

    for i in permutations([a, b, c], r=3):
        if (i[1]-i[0] == i[2]-i[1]) and ((i[1] - i[0]) != 0):
            count += 1
            break


print(count)
