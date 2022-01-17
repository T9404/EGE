def f(x):
    a = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)
    return sum(a)

k = 0
for i in range(150001, 10000000):
    if f(i) % 13 == 10:
        print(i, f(i))
        k+=1
    if k == 7:
        break
