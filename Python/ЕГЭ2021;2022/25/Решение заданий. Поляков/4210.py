def calc_a(n):
    mx_chet, mn_nechet = 0, 10 ** 9999
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d % 2 == 0 and d > mx_chet:
                mx_chet = d
            if d % 2 != 0 and d < mn_nechet:
                mn_nechet = d
            if (n // d) % 2 == 0 and (n // d) > mx_chet:
                mx_chet = n // d
            if (n // d) % 2 != 0 and (n // d) < mn_nechet:
                mn_nechet = n // d
    if mx_chet == 0 or mn_nechet == 10 ** 9999:
        return 0
    else:
        return abs(mx_chet - mn_nechet)


def isPrime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


c = 0
for i in range(250_156 + 1, 10 * 999):
    a = calc_a(i)
    print(a)
    if a != 0 and isPrime(a) and a % 10 == 9:
        print(i, a)
        c += 1
        if c == 5:
            break
