'''
Администратор написал скрипт для раскладки N архивов на K дисков, каждый объемом V. 
Алгоритм скрипта обрабатывает файлы в порядке убывания их размера. Если файл помещается 
на диск, то следующий по размеру файл стараются поместить на следующий диск. Если не 
помещается, то на следующий, и так по кругу. Если файл не поместился ни на один диск, 
то он откладывается в локальную папку. Укажите в ответе два числа: объем всех отложенных 
файлов и их количество.
'''
# https://prnt.sc/LJeDRHdfN6AH


f = open('26.txt')
v, k, n = map(int, f.readline().split())


numbers = [int(x) for x in f]
numbers.sort(reverse=True)


disk = [0] * k
need_num = []


arr = ''
for i in range(k):
    arr += str(i)


for x in numbers:
    count = 0

    for i in arr:
        i = int(i)
        count += 1

        if (disk[i] + x) <= v:
            disk[i] += x
            arr = arr[1:len(arr)] + arr[0]
            break

        elif count == k:
            need_num.append(x)


print(sum(need_num), len(need_num))
