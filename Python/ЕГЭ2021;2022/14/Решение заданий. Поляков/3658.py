def f(x, i):
    x_i = ''

    while x:
        x_i += str(x % i)
        x //= i

    x_i = x_i[::-1]

    for j in range(len(x_i)-1):
        if int(x_i[j]) % 2 == int(x_i[j+1]) % 2:
            return 0

    return i


m = [f(78, j) for j in range(2, 10+1)]
print(sum(m))
