f = open('24 (7).txt')
s = f.readline()

mak = 0
s = s.split('A') 

for i in range(len(s)-1):
    new_str = s[i]+'A'+s[i+1]
    mak = max(len(new_str), mak)

print(mak)
