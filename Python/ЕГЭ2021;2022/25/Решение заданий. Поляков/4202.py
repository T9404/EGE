def isPrime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


c, sr = 0, 0


for i in range(3 * 10 ** 6, 10 ** 7 + 1):
    if isPrime(i) and isPrime(i + 2):
        c += 1
        sr = (2 * i + 2) // 2  # ( i+(i+2))//2


print(c, sr)
