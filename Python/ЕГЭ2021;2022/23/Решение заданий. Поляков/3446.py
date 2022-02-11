a = set()
def f(s, c):
    if c == 4:
        a.add(s)
    elif c < 4:
        f(s+1, c+1)
        f(s+5, c+1)
        f(s*3, c+1)
        
f(1, 0)
print(len(a))
