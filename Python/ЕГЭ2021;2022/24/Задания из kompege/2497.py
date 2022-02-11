f = open('24.txt')
s = f.readline()
k = 0
for i in range(len(s)-4):
    if s[i:i+5] == 'XVIII':
        k+=1
print(k)
