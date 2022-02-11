f = open('24.txt')
s = f.readline()

s = s.replace('C', ' ')
s = s.replace('D', ' ')

mak = 0
for i in s.split():
    mak = max(mak, len(i))
print(mak)

