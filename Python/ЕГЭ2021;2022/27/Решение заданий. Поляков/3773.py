f = open('27-54a.txt')
n = int(f.readline())


number = [0]*4
para = [0]*4
troika = [0]*4

mak = 0

for _ in range(n):
    x = int(f.readline())

    for i in range(4):
        if ((troika[i]+x) % 4 == 0):
            mak = max(troika[i]+x, mak)

    for i in range(4):
        troika[(x+i) % 4] = max(troika[(x+i) % 4], para[i]+x)

    for i in range(4):
        para[(x+i) % 4] = max(para[(x+i) % 4], number[i]+x)

    number[x % 4] = max(number[x % 4], x)

    
print(mak)
