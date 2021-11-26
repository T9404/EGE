a = set()

def f(s, k):
    if (k == 8):
        if ( 1000 <= s <= 1024):
            a.add(s)
    else:
        f(s+1, k+1)
        f(s+5, k+1)
        f(s*3, k+1)
        

f(1, 0)
print(len(a))
