def find_dev(n):
    dev = set()

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            dev.add(i)
            dev.add(n//i)

    if len(dev) >= 5:
        a = sorted(dev)
        return a[0]*a[1]*a[2]*a[3]*a[4], a[4]
    else:
        return 0, 0


i, k = 400_000_000, 0

while k < 5:
    i += 1
    
    if find_dev(i)[0] % 100 == 17 and find_dev(i)[0] < i:
        k += 1
        print(*find_dev(i))
