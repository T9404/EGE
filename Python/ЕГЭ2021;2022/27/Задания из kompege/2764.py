f = open('27B.txt')
n = int(f.readline())


rust = [int(f.readline()) for _ in range(6)]


m = [[float('inf')]*23 for _ in range(6)]  # произведение 6, сумма 23
ans = float('inf')


for _ in range(n-6):
    x = int(f.readline())

    ostat = 0 if (x % 23 == 0) else (23 - (x % 23))

    for i in range(6):
        if (x * i) % 6 == 0:
            if m[i][ostat] != float('inf'):
                ans = min(ans, x + m[i][ostat])

    m[x % 6][x % 23] = min(m[x % 6][x % 23], x)

    rust.append(x)
    rust.pop(0)


print(ans)
