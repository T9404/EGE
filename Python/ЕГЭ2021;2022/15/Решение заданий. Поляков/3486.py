def f(x, y, a):
    return (x**2-3*x+2 > 0) or (y > x**2+7) or (x*y < a)


for a in range(0, 100):
    if all(f(x, y, a) == 1 for x in range(1, 100) for y in range(1, 100)):
        print(a)
        break
