'''
Текстовый файл 24-j5.txt состоит не более чем из 106 символов S, T, O, C, K. 
Определите максимальное количество подряд идущих комбинаций «KOT».
'''
# https://prnt.sc/bbGa4KXcANQI


f = open('24.txt')
s = f.readline()


max_count, count, i = 0, 0, 1


while True:
    try:
        if (s[i-1] == 'K') and (s[i] == 'O') and (s[i+1] == 'T'):
            count += 1
            i += 3
        else:
            max_count = max(max_count, count)
            count = 0
            i += 1
    except:
        break


print(max_count)
