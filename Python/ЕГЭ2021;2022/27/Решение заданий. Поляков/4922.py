f = open('27.txt')
n, k = map(int, f.readline().split())


prefix = [0]*k
s, ans = 0, 0


for _ in range(n):
    x = int(f.readline())
    s += x

    if s % k == 0:
        ans += 1

    ans += prefix[s % k]

    prefix[s % k] += 1


print(ans)
