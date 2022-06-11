'''
В файле 17-3.txt содержится последовательность целых чисел. Элементы последовательности 
могут принимать целые значения от -10 000 до 10 000 включительно. Определите и запишите 
в ответе сначала количество троек элементов последовательности, в которых хотя бы одно 
число кратно 12, а каждое число делится на 3, затем минимальное из средних арифметических 
элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд 
элемента последовательности.
'''
# https://prnt.sc/54kIVEZHqqGh


f = open('17-3.txt')
arr = [int(i) for i in f.readlines()]


def func(d):
    for i in d:
        if (i % 3 != 0):
            return False

    for i in d:
        if (i % 12 == 0):
            return True

    return False


count, min_arif = 0, float('inf')


for i in range(1, len(arr)-1):
    list_num = [arr[i-1], arr[i], arr[i+1]]

    if func(list_num):
        min_arif = min(min_arif, sum(list_num) // 3)
        count += 1


print(count, min_arif)
