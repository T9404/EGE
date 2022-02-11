f = open('27-59b.txt')
n = int(f.readline())


count = [0]*10

for _ in range(n):
    x = int(f.readline())

    dinam = [0]*10

    for i in range(10):
        dinam[(x+i) % 10] += count[i]

    dinam[x % 10] += 1

    for i in range(10):
        count[i] += dinam[i]

        
print(count[5])
