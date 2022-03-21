f = open('24.txt')
s = f.readline()


k = 0

for i in range(1, len(s)-3):
    if s[i-1] != 'J' and s[i] == 'B' and s[i+1] == 'O' and s[i+2] == 'S' and s[i+3] == 'S' and s[i+4] != 'J':
        k += 1

print(k)
