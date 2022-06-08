# Мне не понятно, что именно имел автор. 
# Либо спрашивали про количество делителей, 
# либо про состав числа из делителей, тогда
# нужно будет перебирать для каждого числа произведение делителей


def f(x):
    a = set()
    a.add(1)

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x // i)

    if len(a) <= 3:  # число "1" и еще 2 делителя максимум
        return sorted(a)
    else:
        return None


d = []
t = 0


for k in range(1, 100):
    n = 500_000_000 + k
    if f(n) != None:
        t += 1
        d.append([k, f(n)[-1]])

    if t == 5:
        break


for i in d[::-1]:
    print(*i)
