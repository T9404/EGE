# (I) Решение

f = open('24.txt')
s = f.readline()


k, mak = 1, 1

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        k += 1
    else:
        mak = max(mak, k)
        k = 1

print(mak)



# (II) Решение

f = open('24.txt')
s = f.readline()


while 'XX' in s or 'YY' in s or 'ZZ' in s:
    s = s.replace('XX', 'X X')
    s = s.replace('YY', 'Y Y')
    s = s.replace('ZZ', 'Z Z')


L = len(max((i for i in s.split()), key=len))
print(L)
