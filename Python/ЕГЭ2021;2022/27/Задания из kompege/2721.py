f = open('27B.txt')
n = int(f.readline())


'''  65 = 5 * 13  '''
chet_5, chet_13 = 0, 0
chet_65, other = 0, 0

for _ in range(n):
    x = int(f.readline())

    if x % 65 == 0:
        chet_65 += 1

    elif x % 5 == 0:
        chet_5 += 1

    elif x % 13 == 0:
        chet_13 += 1

    else:
        other += 1


print( (chet_65*(n-chet_65)) + (chet_65*(chet_65-1)//2) + (chet_5*chet_13) )
