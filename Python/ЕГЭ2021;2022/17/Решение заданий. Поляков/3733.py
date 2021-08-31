def ok(n):
    return (n % 7 == 6) and (n % 32 == 0)

a = [n for n in range(15, 1000+1) if ok(n)]
print(len(a), a[-1])
