a = set()

def f(s, k):
    if k == 15:
        a.add(s)
        return 1
    else:
        return f(s*2, k+1)+f(s*2+1, k+1)

f(1, 0)

print(len(a))
