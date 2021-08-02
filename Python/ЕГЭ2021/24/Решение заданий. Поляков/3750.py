'''
Определите символ,
который чаще всего встречается в файле между двумя одинаковыми символами. 
'''

f = open('24-157.txt')
s = f.readline()

symb = [0]*26

for i in range(1, len(s)-1):
    if s[i-1] == s[i+1]:
        symb[ord(s[i])-ord('A')]+=1
mak = 0
for i in range(len(symb)):
    if symb[i] > mak:
        mak = symb[i]
        let = i
print(chr(let+ord('A')), mak)

