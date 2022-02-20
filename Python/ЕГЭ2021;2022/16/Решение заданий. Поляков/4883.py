def prime(x):
    return all(x % i != 0 for i in range(2, int(x**0.5)+1))


def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return 7 * (n - 1) + f(n - 1)


arr = [n for n in range(2, 200+1) if prime(f(n))]

print(len(arr))
