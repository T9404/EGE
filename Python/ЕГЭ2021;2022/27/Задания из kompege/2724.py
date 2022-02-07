f = open('27A.txt')
n = int(f.readline())


prime = all(131 % i != 0 for i in range(2, int(131**0.5)+1))

if prime:
    ostat = [0]*131


for _ in range(n):
    x = int(f.readline())
    ostat[x % 131] += 1


# кратные числа имеют кратную сумму, комба решает "//2"
ans = ostat[0]*(ostat[0]-1) // 2

for i in range(1, 65+1):
    ans += (ostat[i]*ostat[131-i])


print(ans)
