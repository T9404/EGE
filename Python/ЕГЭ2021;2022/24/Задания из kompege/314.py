f = open('24.txt')
s = f.readline()


k = 0

for i in range(len(s)-3):
    # можно делать через каждый символ(без срезов), но это долго :)
    if s[i+2:i+5] == 'OCK':
        if s[i:i+5] != 'STOCK':
            k += 1
            
print(k)
