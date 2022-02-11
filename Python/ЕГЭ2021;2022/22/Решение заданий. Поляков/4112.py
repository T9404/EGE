c=0
for i in range(int("100000", 16), int("FFFFFF", 16)+1):
    x = i
    L, M = 0, 0
    while x > 0:
        L = L + 1
        if x % 16 % 2 == 0:
            M = M + 1
        else:
            M = M - 1
        x = x // 16
    if L==6 and M==0:
        c+=1

print(c)