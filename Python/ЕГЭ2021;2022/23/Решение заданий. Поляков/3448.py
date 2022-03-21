d = set()

def f(start, count):

    if count == 6:
        if (34 <= start <= 59):
            d.add(start)

    if count < 6:
        f(start+1, count+1)
        f(start+2, count+1)
        f(start*2, count+1)

f(1, 0)

print(len(d))
