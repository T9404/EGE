def f(start, end):
    if start > end or start == 20:
        return 0
    elif start == end:
        return 1
    else:
        return f(start+1, end)+f(start*2, end)+f(start*3, end)


print(f(2, 25))
