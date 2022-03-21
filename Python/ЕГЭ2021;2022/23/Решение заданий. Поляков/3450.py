def f(start, end):
    if end < start:
        return 0
    elif start == end:
        return 1
    else:
        return f(start+1, end)+f(start+5, end)+f(start*3, end)


for x in range(1, 1000):
    if f(1, x) == 175:
        print(x)
        break
