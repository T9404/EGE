'''
Текстовый файл содержит только заглавные буквы латинского алфавита(ABC…Z). 
Определите максимальное количество идущих подряд символов, 
среди которых не более одной буквы A.
'''
# https://prnt.sc/6RLSl8xOyNm9


f = open('24.txt')
s = f.readline()

s = s.split('A')


max_string = 0


for i in range(len(s) - 1):
    new_str = s[i] + 'A' + s[i+1]
    max_string = max(len(new_str), max_string)


print(max_string)
