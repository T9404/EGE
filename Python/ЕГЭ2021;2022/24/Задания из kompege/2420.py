'''
В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F. 
Найдите длину самой длинной подцепочки, состоящей из символов A, B, E, F (в произвольном порядке).
'''
# https://prnt.sc/JywmUB1btkao


f = open('24.txt')
s = f.readline()

s = s.replace('C', ' ')
s = s.replace('D', ' ')


max_len = 0


for i in s.split():
    max_len = max(max_len, len(i))

 
print(max_len)
