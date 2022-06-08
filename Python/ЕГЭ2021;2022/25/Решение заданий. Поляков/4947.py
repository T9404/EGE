def uniq(x):
    d = list(str(x))
    new_d = [i for i in d if (int(i) % 2 != 0)]

    return len(new_d) == len(d)


def f(x):
    a = set()

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)

    a = sorted(a)
    a = [i for i in a if uniq(i)]

    if len(a) < 5:
        return 0
    else:
        return a[-5], len(a)


d = []


for i in range(299_999_999, 2, -1):
    if f(i) != 0:
        d.append(f(i))

    if len(d) == 5:
        break


for i in range(len(d)-1, -1, -1): 
    print(*d[i])
