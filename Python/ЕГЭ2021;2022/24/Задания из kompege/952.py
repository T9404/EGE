'''
В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F и 
десятичных цифр. Найдите длину самой длинной подцепочки, не содержащей гласных букв.
'''
# https://prnt.sc/sCn6ncHpbCW_


f = open('24.txt')
s = f.readline()


max_string = float('-inf')


for i in range(1, len(s) - 1):
    if (s[i] != s[i-1]) and (s[i] != s[i+1]):
        j = i + 1
        count = 1

        # не берем последний элемент
        while j < len(s) - 1:
            if s[j] != s[j-1] and s[j] != s[j+1]:
                count += 1
                j += 1
            else:
                break

        max_string = max(count, max_string)


print(max_string)
