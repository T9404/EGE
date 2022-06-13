'''
При проведении эксперимента заряженные частицы попадают на чувствительный экран, представляющий из себя матрицу 
размером 10000 на 10000 точек. При попадании очередной частицы на экран в файл записываются координаты чувствительного 
элемента: номер строки (целое число от 1 до 10000) и номер позиции в строке (целое число от 1 до 10000). Точка экрана, 
в которую попала хотя бы одна частица, считается светлой, точка, в которую ни одна частица не попала, – тёмной.
Вам необходимо по заданному протоколу определить номер строки с наибольшим количеством светлых точек в нечётных позициях. 
Если таких строк несколько, укажите номер первой из подходящих строк.
'''
# https://prnt.sc/3DAxBXbbnygY


f = open('26-82.txt')
n = int(f.readline())


screen = {}


for _ in range(n):
    number_string, position_string = map(int, f.readline().split())

    if number_string in screen:
        screen[number_string].append(position_string)
    else:
        screen[number_string] = [position_string]


max_len, strin_mak = float('-inf'), float('inf')


for m in screen:
    arr = sorted(set(screen[m]))
    len_arr = len([i for i in arr if (i % 2 != 0)])
    if (max_len < len_arr) or (max_len == len_arr and strin_mak > m):
        max_len = len_arr
        strin_mak = m


print(max_len, strin_mak)
