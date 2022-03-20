f = open('17-3.txt')


a = [int(x) for x in f.readlines()]


def f(d):
    for i in d:
        if i % 3 != 0:
            return False

    for i in d:
        if i % 12 == 0:
            return True

    return False


mik, k = float('inf'), 0


for i in range(1, len(a)-1):
    d = [a[i-1], a[i], a[i+1]]

    if f(d):
        mik = min(mik, sum(d)//3)
        k += 1


print(k, mik)
