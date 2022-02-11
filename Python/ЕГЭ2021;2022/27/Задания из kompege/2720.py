f = open('27B.txt')
n = int(f.readline())


chet_7 = 0

for _ in range(n):
    x = int(f.readline())

    if x % 7 == 0:
        chet_7 += 1


nechet_7 = n - chet_7

print( (nechet_7*chet_7) + (chet_7*(chet_7-1)//2) )
