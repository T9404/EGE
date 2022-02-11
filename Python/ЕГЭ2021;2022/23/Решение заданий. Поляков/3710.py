def f(start, end):
    if start == end:
        return 1
    elif int(start, 2) > int(end, 2):
        return 0
    else:
        rez = int(start, 2) + 1
        return f(bin(rez)[2:], end)+f(start+'0', end)+f(start+'1', end)


print(f('101', '101110'))
