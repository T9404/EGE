f = open('24 (7).txt')

s = f.readline()
s = s.split('A')


mak = 0

for i in range(len(s)-1):
    new_str = s[i]+'A'+s[i+1]
    mak = max(len(new_str), mak)

print(mak)
