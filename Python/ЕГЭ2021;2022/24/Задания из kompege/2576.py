f = open('24.txt')
s = f.readline()


arr = s.split('.')
mak = float('-inf')


for strin in arr:
    if strin.count('A') >= 3:
        mak = max(mak, len(strin))


print(mak)
