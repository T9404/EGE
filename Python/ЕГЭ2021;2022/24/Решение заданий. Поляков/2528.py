'''
Текстовый файл 24-1.txt состоит не более чем из 106 символов - заглавных латинских букв и цифр. 
Определите максимальное число, состоящее только из чётных цифр. Под числом подразумевается 
последовательность цифр, ограниченная другими символами (не цифрами).
'''
# https://prnt.sc/M-suRpzqwIT5


f = open('24.txt')
s = f.readline()


def F(n):
    for i in range(len(n)):
        if (int(n[i]) % 2 == 1):
            return False
    return True


for i in range(ord('A'), ord('Z') + 1):
    s = s.replace(chr(i), ' ', s.count(chr(i)))


print(max(int(x) for x in s.split() if (F(x) == True)))
