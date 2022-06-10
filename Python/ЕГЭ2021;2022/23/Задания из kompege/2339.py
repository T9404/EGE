# (I) Решение

a = set()

def f(s, k):
    if k == 15:
        a.add(s)
        return 1
    else:
        return f(s*2, k+1)+f(s*2+1, k+1)

f(1, 0)
print(len(a))


# (II) Решение

d = [1]

for _ in range(15): # 15 команд
    for j in range(len(d)):
        m = d.pop(0)
        d.append(2 * m)
        d.append(m * 2 + 1)

print(len(d))
