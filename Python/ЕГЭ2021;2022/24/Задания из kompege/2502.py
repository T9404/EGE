'''
Текстовый файл состоит не более чем из 106 заглавных латинских букв (A..Z). 
Текст разбит на строки различной длины. Определите количество строк, в которых хотя 
бы раз встречается комбинация K*GE, где звёздочка означает произвольный символ.
'''
# https://prnt.sc/UO_CyrqZiEbr


f = open('24.txt')
s = f.readlines()


def check_str(strin):
    for i in range(1, len(w) - 2):
        if (strin[i-1] == 'K') and (strin[i+1:i+3] == 'GE'):
            return True

    return False


count = 0


for w in s:
    if check_str(w):
        count += 1


print(count)
