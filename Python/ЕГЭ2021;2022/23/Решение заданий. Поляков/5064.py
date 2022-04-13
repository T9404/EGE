from math import gcd


a = set()


def f(s, e, count):
    if count > 5:
        return 0
        
    elif count == 5 and gcd(s, e) == 1 and ((s, e) not in a) and ((e, s) not in a):
        a.add((s, e))

    else:
        f(s+3, e, count+1)
        f(s*4, e, count+1)
        f(s, e + 5, count+1)
        f(s, e*2, count + 1)


f(2, 3, 0)
print(len(a))
