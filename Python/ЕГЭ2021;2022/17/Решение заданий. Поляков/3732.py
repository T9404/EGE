def ok(n):
    return (n % 10 == 9) and (n % 8 == 1) and\
        (n % 18 != 0)

a = [x for x in range(99, 998+1) if ok(x)]
print(len(a), a[-1])