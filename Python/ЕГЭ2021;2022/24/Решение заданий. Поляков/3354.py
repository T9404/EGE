'''
Текстовый файл 24-4.txt содержит последовательность из строчных и заглавных букв английского 
алфавита и цифр, всего не более 106 символов. Убывающей подпоследовательностью будем называть 
последовательность символов, расположенных в порядке уменьшения их номера в кодовой таблице 
символов ASCII. Запишите в ответе наибольшую убывающую подпоследовательность. 
Если таких последовательностей несколько, запишите первую из них.
'''
# https://prnt.sc/FuvpK5C9d8cB


f = open('24.txt')
s = f.readline()


string = s[0]
max_string = ''


for i in range(len(s) - 1):
    if (s[i] > s[i+1]):
        string += s[i+1]
        if (len(max_string) < len(string)):
            max_string = string
    else:
        string = s[i+1]


print(max_string)
