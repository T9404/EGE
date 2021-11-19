def f(x):
    a = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)
    if len(a) < 5:
        return 0, 0
    else:
        b = sorted(list(a))
        p_n = b[0]*b[1]*b[2]*b[3]*b[4]
        return  p_n, b[4]

k = 0

for i in range(500000001, 600000001, 1):
    p_n, num = f(i)
    
    if p_n % 100 == 91  and p_n <= i:
        k += 1
        print(p_n, num)

    if k == 5:
        break
