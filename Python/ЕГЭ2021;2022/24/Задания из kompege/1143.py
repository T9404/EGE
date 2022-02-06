f = open('24_1.txt')
s = f.readline()


k = 0

for i in range(len(s)-10):
    if s[i] == 'A':
        
        for j in range(6, 9+1):
            if s[i+j] == 'F':
                k += 1

print(k)
