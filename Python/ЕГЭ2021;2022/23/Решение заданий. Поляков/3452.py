def f(start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        return f(start+2, end)+f(start+4, end)+f(start+5, end)

for i in range(1, 10000):
    if f(31, i) == 1001:
        print(i)
        break
