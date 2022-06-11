'''
В файле содержится последовательность целых чисел. Элементы последовательности 
могут принимать целые значения от 0 до 10 000 включительно. Рассматривается 
множество элементов последовательности, которые делятся на 3 и не делятся 
на 7, 17, 19, 27. Найдите количество таких чисел и максимальное из них.
'''
# https://prnt.sc/nmOwXEaAaOzR


f = open('17.txt')
arr = [int(x) for x in f.readlines()]


max_elem, count = 0, 0

for i in range(len(arr)):
    if (arr[i] % 3 == 0 and arr[i] % 7 != 0 and arr[i] % 17 != 0 
            and arr[i] % 19 != 0 and arr[i] % 27 != 0):
        count += 1
        max_elem = max(arr[i], max_elem)


print(count, max_elem)
