f = open('17.txt')
n = 5000

a = [int(f.readline()) for _ in range(n)]
k, mak = 0, 0

for i in range(1, n):
<<<<<<< HEAD
    if (a[i-1] + a[i]) % 3 == 0:

        if (a[i-1]+a[i]) % 6 != 0:

            if abs(a[i]*a[i-1]) % 10 == 8:
                mak = max(mak, a[i-1]+a[i])
                k += 1

=======
    if ((a[i-1] + a[i]) % 3 == 0 and
            (a[i-1]+a[i]) % 6 != 0 and
            abs(a[i] * a[i-1]) % 10 == 8):
        mak = max(mak, a[i-1]+a[i])
        k += 1
>>>>>>> 2c133933b4655bc5abd8a7c5d7aeb96e63b9db0f

print(k, mak)
