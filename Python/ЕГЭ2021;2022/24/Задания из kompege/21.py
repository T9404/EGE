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
