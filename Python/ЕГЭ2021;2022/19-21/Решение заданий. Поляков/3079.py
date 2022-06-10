def f(a, c, m):
    if a > 33:
        return c % 2 == m % 2
    if c == m:
        return 0
    
    h = [f(a+1, c+1, m), f(a+2, c+1, m), f(a+3, c+1, m), f(a*2, c+1, m)]

    return any(h) if (c+1) % 2 == m % 2 else all(h)


t19, t20, t21, t1 = [], [], [], []


for s in range(1, 34):
    for m in range(1, 6):
        if f(s, 0, m) == 1:
            if m == 1:
                t1.append(s)
            if m == 2:
                t19.append(s)
            if m == 3 and not s in t1:
                t20.append(s)
            if m == 4 and not s in t19:
                t21.append(s)

                
print(t19[0])
print(min(t20), max(t20))
print(t21[0])
