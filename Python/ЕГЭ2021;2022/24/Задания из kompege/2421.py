f = open('24 (1).txt')
s = f.readline()

s = s.replace('D', ' ')
mak = 0

for i in s.split():
    mak = max(len(i), mak)
print(mak)
