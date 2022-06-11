'''
Демоверсия 2021
Текстовый файл состоит не более чем из 106 символов X, Y и Z.  
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны. 
Для выполнения этого задания следует написать программу. 
'''
# https://prnt.sc/HcL5eBNtmhWZ


# (I) Решение

f = open('24.txt')
s = f.readline()


count, max_string = 1, 1


for i in range(1, len(s)):
    if s[i-1] != s[i]:
        count += 1
    else:
        max_string = max(max_string, count)
        count = 1


print(max_string)



# (II) Решение

f = open('24.txt')
s = f.readline()


while 'XX' in s or 'YY' in s or 'ZZ' in s:
    s = s.replace('XX', 'X X')
    s = s.replace('YY', 'Y Y')
    s = s.replace('ZZ', 'Z Z')


answer = len(max((i for i in s.split()), key=len))
print(answer)
