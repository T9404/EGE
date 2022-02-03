f = open('24-179.txt')
s = f.readline()


k = 0
a = [0]*26

for i in range(len(s)-4):
    if s[i] == 'C' and s[i+1] == 'A' and s[i+2] not in ['A', 'B', 'F'] and s[i+3] == 'A' and s[i+4] == 'C':
        k += 1
        a[ord(s[i+2])-ord('A')] += 1

print(chr(ord('A')+a.index(max(a))), k)
