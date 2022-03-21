def find_s2(n):
    n_2 = str(n)[::-1]
    a = ''

    for i in range(0, len(n_2), 2):
        a += n_2[i]

    return sum(map(int, a))


def f(n):
    s1 = sum([int(i) for i in str(n) if int(i) % 2 == 0])
    s2 = find_s2(n)
    
    return abs(s1-s2)


for i in range(1, 10000000):
    if f(i) == 26:
        print(i)
        break
