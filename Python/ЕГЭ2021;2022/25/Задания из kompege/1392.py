def f(x):
    a = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)
    if a:
        return sum(a) // len(a)
    else:
        return 0

k = 0
i = 550000
while k < 5:
    i += 1
    if f(i) % 31 == 13:
        k += 1
        print(i, f(i))

        
    
