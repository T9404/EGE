a = []


def f(start, k):
    if start == 22 and k == 7:
        a.append(start)

    if k < 7:
        f(start+1, k+1)
        f(start+2, k+1)
        f(start+3, k+1)


f(3, 0)
print(len(a))
