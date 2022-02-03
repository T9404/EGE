f = open('24 (3).txt')

s = f.readline()
s = s.replace('A', ' ')
s = s.replace('B', ' ')
s = s.replace('C', ' ')


mak = 0

for i in s.split():
    mak = max(mak, len(i))

print(mak)
